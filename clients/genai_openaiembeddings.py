from langchain_openai import OpenAIEmbeddings
import os

def create_embedding():
  return OpenAIEmbeddings(
    model='text-embedding-3-large',
    openai_api_key=os.environ['API_KEY']
  )