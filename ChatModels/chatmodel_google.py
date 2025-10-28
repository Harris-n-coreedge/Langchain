from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=1.7)
result = model.invoke("What is the capital of India?")
print(result.content)  