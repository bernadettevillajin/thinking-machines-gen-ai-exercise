### ADA (Augmented Data Assistant) - Project Journal

#### **Project Overview**
ADA (Augmented Data Assistant) is a prototype AI-powered tool designed to answer user questions using information from an uploaded PDF document. It leverages advanced AI technologies to extract knowledge, convert it into embeddings, and store it in a vector database for efficient retrieval, enabling accurate responses through a chat interface.

#### **Main Technologies Used**
- **Chroma:** A vector database to store document embeddings for fast retrieval.
- **LangChain:** Utilized for building conversational agents, specifically using the `ConversationalRetrievalChain` for handling interactions.
- **ChatOpenAI (`gpt-4o`):** The language model used to process user inquiries and provide answers.
- **OpenAIEmbeddings (`text-embedding-3-large`):** Generates high-quality embeddings of document content to represent them as vectors.
- **PyMuPDF:** The `LlamaMarkdownReader` from `PyMuPDF4LLM` was used to load and read PDF documents, providing structured output optimized for LLM and RAG environments with seamless support for LlamaIndex integration.

#### **Pipelines**

The system is composed of two primary pipelines:

1. **`build_chain`:** Triggers when a user uploads a PDF document.
    - This pipeline processes the uploaded document, extracts embeddings, initializes a vector store, and builds a chain for querying.
    - **Code Breakdown:**

    ```python
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
    ```

    - **Explanation:**
        - `load_data(file)`: This function loads the PDF document and returns a list of documents (structured data) and a collection name for the document.
        - `create_embedding()`: Creates embeddings using OpenAI’s `text-embedding-3-large` model.
        - `initialize_vector_store(documents, embeddings, collection_name)`: Initializes a Chroma vector store to store document embeddings.
        - `build_chain(get_model(), vectordb)`: Builds the LangChain `ConversationalRetrievalChain` using the GPT-4 model and the vector store.

2. **`process_question`:** Triggers when a user submits a question through the chat interface.
    - **Code Breakdown:**

    ```python
    def process(chain, question, chat_history):
        res = chain.invoke({
            'question': question,
            'chat_history': chat_history
        })
        return res['answer']
    ```

    - **Explanation:**
        - `chain.invoke()`: The function calls the chain, providing the user’s question and chat history as inputs. It retrieves a response from the GPT-4 model, which is then returned as the answer.

#### **Helper Functions**

1. **`collection_name_cleaner`:** Cleans the collection name for use in the vector store.
    - **Code Breakdown:**

    ```python
    import re
    from datetime import datetime

    def clean(name):
        name = f"{name.split('.')[0].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        allowed_chars = re.sub(r'[^a-zA-Z0-9-_]', '', name)
        return allowed_chars[:63]
    ```

    - **Explanation:**
        - This function processes the `name` of the collection by removing spaces, adding a timestamp to ensure uniqueness, and adhering to the format of a valid collection name. It restricts the characters to alphanumeric and a few special characters (`-`, `_`), truncating the result to 63 characters.

2. **`metadata_cleaner`:** Cleans the metadata associated with the documents.
    - **Code Breakdown:**

    ```python
    from langchain.schema import Document
    from langchain_community.vectorstores.utils import filter_complex_metadata

    def clean(metadata):
        return filter_complex_metadata(metadata) if isinstance(metadata, Document) else {}
    ```

    - **Explanation:**
        - This function filters out complex metadata if the metadata is an instance of a `Document` object, ensuring that only relevant and clean metadata is retained.

3. **`prompt_template`:** Constructs a template for generating a prompt, including the user’s inquiry.
    - **Code Breakdown:**

    ```python
    def get_template(inquiry):
        return f"""
        You are a friendly guide addressing people's inquiries.
        ## Given this inquiry: {inquiry}

        **Assess whether the inquiry is just a casual greeting or not**
        - **If inquiry is just a casual greeting:**
          - Respond in a warm and user-friendly tone to make the interaction pleasant.

        - **If inquiry is not a casual greeting:**
          - **Assess whether the inquiry is relevant to the documents and previous chat histories**
            - **If the inquiry is relevant to the documents and previous chat histories:**
              - Respond concisely, in English language, with regular fonts, and clarity while reflecting the document's information.
              - Use data, examples, and narratives from the document—may it be in text, tabular, or graphical form—to best represent your point.

            - **If the inquiry is not relevant to the documents and previous chat histories:**
              - Politely say you are not allowed to disclose such information.
        """
    ```

    - **Explanation:**
        - This function generates a structured prompt in **Markdown format** to optimize AI response generation. Markdown is used for its ability to define sections clearly, apply consistent formatting (e.g., headers, bullet points), and emphasize key instructions, ensuring precise parsing by language models. The prompt explicitly outlines how the AI should handle document-based inquiries, detailing response criteria and structure for accurate, context-aware outputs.

#### **Docker Setup**

The project is containerized using **Docker** to ensure consistent execution across environments. The setup includes:

- **`docker-compose.yml`**
- **`Dockerfile`**
- **`requirements.txt`**: Specifies Python dependencies, automatically installed during the Docker setup.

This approach guarantees portability, scalability, and easy deployment.

#### **Entry point: `index.py`**

The project is built entirely in **Python**, with the **`index.py`** file serving as the main entry point. This file manages user interactions, handles PDF uploads, and processes inquiries, all within a single unified Python environment.

#### **Personalization**

The project includes the **Thinking Machines Data Science** logo for personalization and branding.

#### **Improvements and Future Considerations**

- **Prototype-only limitations**: The current version of ADA is designed to function under an ideal scenario, i.e., supports only one PDF document per session. When uploading a new file, a Docker rebuild is required to ensure proper processing and integration, reflecting the prototype’s focus on simplicity and core functionality.
- **Static models**: The models used in the system are static; consequently, the parameters of the LLM model are not adjustable during runtime.

#### **Conclusion**

**ADA** is an initiative that demonstrates the capabilities of **Generative AI**, aligning with the cutting-edge trends shaping the industry today.