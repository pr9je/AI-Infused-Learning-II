import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-oss-120b",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

prompt = ChatPromptTemplate([
  ("system", "You are a friendly assistant. Use the conversation history to stay consistent."),
  MessagesPlaceholder("history"),
  ("human", "{question}")  
])

chain = prompt | model

history = [] # starts EMPTY - nothing hardcorded.

print("Chat with the bot (type 'quit' to exit).")
while True:
    question = input("You: ")
    if question.strip().lower() in {"quit", "exit"}:
        break

    answer = chain.invoke(
        {"history": history, "question": question}).content
    print("Bot:", answer)

    history.append(HumanMessage(question)) # remember the human's question
    history.append(AIMessage(answer)) # and what it replied.
    print(f"    (history now has {len(history)} messages)")