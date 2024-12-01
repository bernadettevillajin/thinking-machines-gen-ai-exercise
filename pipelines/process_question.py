def process(chain, question, chat_history):
  res = chain.invoke({
    'question': question,
    'chat_history': chat_history
  })
  return res['answer']