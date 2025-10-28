from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

result = llm.invoke("What is the capital of India")

print(result)