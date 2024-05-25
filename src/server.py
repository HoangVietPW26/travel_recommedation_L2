import uvicorn

from app import app
from config import Configuration

if __name__ == "__main__":
    host = Configuration.APP_HOST
    port = Configuration.APP_PORT
    uvicorn.run(app, host=host, port=port)
