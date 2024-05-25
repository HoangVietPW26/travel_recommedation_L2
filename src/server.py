import uvicorn

from app import app
from config import Configuration

if __name__ == "__main__":
    APP_HOST = Configuration.APP_HOST
    APP_PORT = Configuration.APP_PORT
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
