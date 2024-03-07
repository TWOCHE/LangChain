# Create OpenAI Function Runnable Chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatMessagePromptTemplate,ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional
from langchain.chains.openai_functions import create_openai_fn_runnable

import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai=os.getenv("openai_apikey")

class Person(BaseModel):
    """identifying information about a person"""

    name: str = Field(...,description="Name of person")
    age: int =Field(...,description="Age of person")
    occupation: Optional[str] =Field(None,description="Occupation of person")

class City(BaseModel):
    """identifying information about a city"""

    name: str = Field(...,description="Name of city")
    Number_plate: int =Field(...,description="Number_plate of city")
    climate: Optional[str] =Field(None,description="climate of city")   


llm=ChatOpenAI(api_key=my_key_openai, model="gpt-3.5-turbo")


prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are the world's most successful algorithm for saving the entities"),
        ("human", "Call the necessary functions to save the entities in the input which I gave you: {input}"),
        ("human","Hint: Make sure you answer in the correct format")
    ]
)

chain_2=create_openai_fn_runnable([Person,City],llm,prompt)

print(chain_2.invoke({"input":"Aydın is a 34-year-old successfully computer engineer"}))
print(chain_2.invoke({"input":"The weather is always hot in Aydın and that's why the air conditioning is always on in vehicles with 09 plate number"}))