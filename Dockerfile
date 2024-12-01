FROM python:3.12-slim-bookworm as builder

RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "index.py", "--server.port", "8501"]