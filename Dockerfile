FROM python:3.9.5

WORKDIR /app

RUN apt-get update 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

EXPOSE 3000

CMD ["python", "src/server.py"]