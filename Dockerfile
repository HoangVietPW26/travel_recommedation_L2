FROM python:3.9.5

WORKDIR /app

ENV PYTHONPATH=.

ENV APP_HOST=0.0.0.0

RUN echo "APP_HOST is ${APP_HOST}"

ENV OPENAI_API_KEY=your_openai_api_key

RUN echo "OPENAI_API_KEY is ${OPENAI_API_KEY}"

RUN apt-get update 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

CMD ["python", "src/server.py"]
