from langchain_anthropic import  ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model= ChatAnthropic(model="Sonnet 4.5", temperature=0.7)
result = model.invoke("What is the capital of India")
print(result.content)
