# we have reviews of different mobile phone we need a dictionary in which we have a key "Summary": that wil
#Generate a summary and second key is Sentiment that will give a sentiment of the review, positive nagitive or neutral
 
from langchain_google_vertexai import ChatVertexAI
from typing import TypedDict, Annotated, Optional,Literal

load_dotenv()

model = ChatVertexAI(model_name="gemini-flash-1.5", temperature=1)
#Schema

class Review(TypedDict):
    key_themes: Annotated[list[str], "The key themes discussed in the review"]
    summary: Annotated[str, "A concise summary of the review"]
    sentiment: Annotated[Literal[["pos","neg","neutral"]], "The sentiment of the review (positive, negative, neutral)"]
    pros: Annotated[Optional[list[str]], "The positive aspects mentioned in the review"]
    cons: Annotated[Optional[list[str]], "The negative aspects mentioned in the review"]
    name: Annotated[Optional[str], "The name of the reviewer"]

structured_output = model.with_structured_output(Review)

result = structured_output.invoke(
    """
“An absolute beast of a phone! The camera is insane especially the 100x zoom, which actually works well in daylight. 
Battery easily lasts me through the day even with heavy use. The display is bright, sharp, and smooth.
Samsung really nailed it with this one. Pricey, but worth every penny if you love premium devices.”
  """
)

print(result)
print(result['summary'])
print(result['sentiment'])
print(result['name'])



