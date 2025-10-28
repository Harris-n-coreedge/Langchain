from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.outputparsers import StucturedOutputParser

load_dotenv()  # Load environment variables from .env file

# Initialize LLM endpoint
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-7B-Chat-GGUF",  # Removed leading slash
    task="text-generation",
)

# Wrap LLM with chat interface
model = ChatHuggingFace(llm=llm)

parser = JSONOutputParser()
# Define PromptTemplate 1

schema = [
    ResponseSchema(name="fact1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = "Give me 3 facts about 5he{topic} \n {format_instruction}",
    input_variables = ['topic'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic': 'Langchain applications'})
# result = model.invoke(prompt)
# print("LLM Output", result.content)

chain = template | model | parser
result = chain.invoke({'topic': "Langchain applications"})
print('result:', result)

print ("Testing the branch")