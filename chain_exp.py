# Create stuff documents chain
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai=os.getenv("openai_apikey")

llm=ChatOpenAI(api_key=my_key_openai, model="gpt-3.5-turbo")

prompt=ChatPromptTemplate.from_messages(
    [("system","Write down the favorite food of the people mentioned here, one by one:\n{context}")]
)

docs=[
    Document(page_content="Gamora likes cheese but doesn't like vegetables."),
    Document(page_content="Mike likes fruit but not as much as he likes fish."),
    Document(page_content="If you ask Benjamin, he would say he doesn't have a favorite food, but he obviously likes red meat.")
]

chain_1=create_stuff_documents_chain(llm,prompt)

print(chain_1.invoke({"context":docs}))


