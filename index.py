import streamlit as st
from pipelines import build_chain, process_question
from helpers import prompt_template
import os

if 'page_loaded' not in st.session_state:
  st.session_state.page_loaded = False

if 'chain' not in st.session_state:
  st.session_state.chain = None

if 'chat_history' not in st.session_state:
  if 'API_KEY' in os.environ:
    del os.environ['API_KEY']

  st.session_state.chat_history = []

@st.dialog('OpenAI API Key')
def register_key():
  st.session_state.page_loaded = True
  st.write('This is essential in utilizing the model capabilities.')
  key = st.text_input('API Key*', type='password')
  if st.button('Register') and key:
    os.environ['API_KEY'] = key
    st.rerun()

st.set_page_config(page_title='ADA', page_icon='🤖', layout='wide')

with st.sidebar:
  st.image('./tm.png')

  if 'API_KEY' not in os.environ:
    if st.button('Register API Key', type='primary', use_container_width=True):
      register_key()

  file = st.file_uploader('Upload your .pdf file', type='pdf', disabled='API_KEY' not in os.environ)
  if file is not None and st.session_state.chain is None:
    with st.spinner('Please wait while we read and understand the content of your file.'):
      with open(file.name, 'wb') as f:
        f.write(file.getbuffer())
        st.session_state.chain = build_chain.build(file.name)
        st.success('You can now start asking questions to our chatbot!')

  st.divider()

  st.markdown("""
  ### 🤖 Conversational Retrieval Chain
  - **Model:** `gpt-4o`
  - Contextual retrieval and conversation

  ### 🧠 OpenAI Embeddings
  - **Model:** `text-embedding-3-large`
  - High-quality text embedding for semantic similarity
  """)

for user, assistant in st.session_state.chat_history:
  if user != 'system':
    with st.chat_message('user'):
      st.markdown(user)
    with st.chat_message('assistant'):
      st.markdown(assistant)

if st.session_state.chain is not None:
  if question := st.chat_input('Hi, what can I help you with?'):
    with st.chat_message('user'):
      st.markdown(question)

    with st.spinner('Analyzing..'):
      response = process_question.process(st.session_state.chain, prompt_template.get_template(question), st.session_state.chat_history)
      with st.chat_message('assistant'):
        st.markdown(response)

      st.session_state.chat_history.append((question, response))

else:
  st.title('🤖 Hello from ADA!')
  st.subheader('Your Friendly Augmented Data Assistant')
  st.write("I'm here to answer your questions using the knowledge from your uploaded PDF.")

  st.divider()
  
  st.header('🚀 How to Get Started')
  st.write(
      """
      1. **Register your OpenAI API key** (if you haven't already).
      2. **Upload a PDF file** using the sidebar on the left.
      3. **Ask questions** about the content of the uploaded PDF file.
      """
  )

  st.info('Tip: Use a PDF file with relevant information for the best experience.')

if 'API_KEY' not in os.environ and not st.session_state.page_loaded:
  register_key()