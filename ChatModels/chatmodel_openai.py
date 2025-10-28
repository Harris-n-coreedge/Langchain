from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

LLM= OpenAI(model_name="text-davinci-003", temperature=0.7)
chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

model.invoke("What is the cspital of India
print(result)")
chat_result = chat_model.invoke("WIndiahat is the capital of ")
print(chat_result)

