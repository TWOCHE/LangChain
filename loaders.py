# WebBaseLoader - loading content from a URL

from langchain_community.document_loaders import WebBaseLoader

target_url="https://www.promptingguide.ai/techniques/rag"

loader=WebBaseLoader(target_url)

raw_documents=loader.load()

with open("URL_content.txt","w") as file:
    file.write(raw_documents[0].page_content)

print("Document operation completed!")

print(raw_documents[0].metadata)
{'source': 'https://www.promptingguide.ai/techniques/rag', 'title': 'Retrieval Augmented Generation (RAG) | Prompt Engineering Guide ', 'language': 'en'}

# PyPDFLoader - loading content from a PDF File

from langchain_community.document_loaders import PyPDFLoader

#loader = PyPDFLoader("example_data/layout-parser-paper.pdf") -----local pdf file 

loader = PyPDFLoader("https://arxiv.org/pdf/2103.15348.pdf", extract_images=True)

pages = loader.load()

print(pages[3].page_content)


# UnstructuredExcelLoader -loading content from a Excel file

from langchain_community.document_loaders import UnstructuredExcelLoader

filepath= "./sample__order_reviews_dataset.xlsx"

loader=UnstructuredExcelLoader(filepath,mode="elements")

docs=loader.load()

excel_content=docs[0].metadata["text_as_html"]

with open("excel.html","w") as file:
    file.write(excel_content)

print("Document operation completed!")
