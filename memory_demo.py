import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-oss-120b",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly tutor."),
    MessagePlaceholder("history"),
    ("human", "{question}"),
])

chain = prompt | model

# we hardcode the history here just to demonstrate.
history = [ HumanMessage("My name is Aarav"), AIMessage("Hi, Aarav!")]

answer = chain.invoke({"history": history, "question": "What is my name?"})
print(answer.content)