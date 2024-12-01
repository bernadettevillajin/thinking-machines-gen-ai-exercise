
# ADA - Augmented Data Assistant

ADA (Augmented Data Assistant) is a chatbot built using Streamlit that answers questions based on the knowledge extracted from an uploaded PDF.

## Prerequisites

- Docker Desktop
- Unexpired OpenAI API key

## Steps to Run the Project

1. Clone this repository to your local machine.
2. Build the Docker image:

   ```bash
   docker-compose build
   ```

3. Run the application:

   ```bash
   docker-compose up
   ```

4. Once the container is running, open your web browser and go to:

   ```
   http://localhost:8501/
   ```

   You should then be able to see the ADA web interface.
