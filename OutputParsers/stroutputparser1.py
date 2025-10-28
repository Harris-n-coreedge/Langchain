from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.outputparsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Initialize LLM endpoint
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-7B-Chat-GGUF",  # Removed leading slash
    task="text-generation",
)

# Wrap LLM with chat interface
model = ChatHuggingFace(llm=llm)

# Define PromptTemplate 1
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

# Define PromptTemplate 2
template2 = PromptTemplate(
    template="Write a 5-line summary of the following text:\n\n{text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'Langchain and its applications'})

print("Chain result:", result)  