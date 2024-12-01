from langchain.chains import ConversationalRetrievalChain

def build_chain(model, vector_store):
  return ConversationalRetrievalChain.from_llm(
    model,
    retriever=vector_store.as_retriever(search_kwargs={'k': 1}),
    return_source_documents=True
  )