import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from scraper import fetch_website_contents

load_dotenv()

# ① a reusable prompt with a {website} blank
prompt = ChatPromptTemplate.from_template(
    "Give a short, friendly summary of this website:\n\n{website}"
)

# ② the same model from Class 1, wrapped for LangChain
model = ChatOpenAI(
    model="openai/gpt-oss-120b",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# ③ the package-opener: hands back plain text
parser = StrOutputParser()

# ④ snap them together  (| means "then")
chain = prompt | model | parser


def summarize(url):
    # ⑤ run it; the dict fills the {website} blank by name
    return chain.invoke({"website": fetch_website_contents(url)})


if __name__ == "__main__":
    print(summarize("https://anthropic.com"))