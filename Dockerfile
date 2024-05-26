FROM python:3.9.5

WORKDIR /app

ENV PYTHONPATH=.

RUN apt-get update 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "server.py"]
