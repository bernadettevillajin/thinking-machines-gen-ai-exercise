from langchain_openai import ChatOpenAI
import os

def get_model():
  return ChatOpenAI(
    model='gpt-4o',
    temperature=0.0,
    openai_api_key=os.environ['API_KEY']
  )