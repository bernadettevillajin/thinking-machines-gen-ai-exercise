from langchain_community.vectorstores import Chroma

def initialize_vector_store(documents, embeddings, collection_name):
  return Chroma.from_documents(
    documents,
    embeddings,
    collection_name=collection_name,
  )