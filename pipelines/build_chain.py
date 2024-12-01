from clients.genai_pymupdf4llm import load_data
from clients.genai_openaiembeddings import create_embedding
from clients.genai_chroma import initialize_vector_store
from clients.genai_langchain import build_chain
from clients.genai_openai import get_model

import logging
logging.basicConfig(level=logging.INFO)

def build(file):
  documents, collection_name = load_data(file)
  logging.info('✓ Data loaded')
  embeddings = create_embedding()
  logging.info('✓ Embedding created')
  vectordb = initialize_vector_store(documents, embeddings, collection_name)
  logging.info('✓ Vector store initialized')
  built_chain = build_chain(get_model(), vectordb)
  logging.info('✓ Chain built')
  return built_chain