import pymupdf4llm
from langchain.schema import Document
from helpers import metadata_cleaner, collection_name_cleaner

def load_data(file):
  md_read = pymupdf4llm.LlamaMarkdownReader()
  data = md_read.load_data(file)
  documents = [
    Document(
      page_content=doc.text,
      metadata=metadata_cleaner.clean(doc.metadata)
    ) for doc in data
  ]
  collection_name = collection_name_cleaner.clean(file)
  return documents, collection_name