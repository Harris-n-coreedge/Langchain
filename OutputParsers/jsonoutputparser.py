from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

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
template = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables=['format_instruction'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template | model | parser
result = chain.invoke({})
print("Result:", result)



