import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI ChatGPT 

my_key_openai=os.getenv("openai_apikey")

from langchain_openai import ChatOpenAI

def ask_gpt(prompt,temperature, max_tokens):

    llm = ChatOpenAI(api_key=my_key_openai,temperature=temperature,max_tokens=max_tokens,model="gpt-3.5-turbo")

    AI_Response=llm.invoke(prompt)

    return AI_Response.content


# Google GEMINI PRO 

my_key_google=os.getenv("google_apikey")

from langchain_google_genai import ChatGoogleGenerativeAI

def ask_gemini(prompt,temperature):

    llm = ChatGoogleGenerativeAI(google_api_key=my_key_google,temperature=temperature,model="gemini-pro")

    AI_Response=llm.invoke(prompt)

    return AI_Response.content


# ANTHROPIC claude 2.1

my_key_anthropic=os.getenv("anthropic_apikey")

from langchain_community.chat_models import ChatAnthropic

def ask_anthropic(prompt,temperature, max_tokens):

    llm = ChatAnthropic(anthropic_api_key=my_key_anthropic,temperature=temperature,max_tokens=max_tokens,model_name="claude-2.1")

    AI_Response=llm.invoke(prompt)

    return AI_Response.content

# COHERE Command

my_key_cohere=os.getenv("cohere_apikey")

from langchain_community.chat_models import ChatCohere

def ask_command(prompt,temperature, max_tokens):

    llm = ChatCohere(cohere_api_key=my_key_cohere,temperature=temperature,max_tokens=max_tokens,model_name="command")

    AI_Response=llm.invoke(prompt)

    return AI_Response.content
