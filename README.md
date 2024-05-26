# Travel-recommendation-L2

## Setup steps and run

## 1. Setup the project directory
* Download `Docker Desktop`, recommend version `4.29.0`, check Docker release note `https://docs.docker.com/desktop/release-notes/` for versions.
* Download `python` version `3.9.5` if you do not want to run project with Docker
* Go to your chosen project folder
* Clone the repository `git clone https://github.com/HoangVietPW26/travel_recommedation_L2`.

## 2. Setup environment variables
* Go to your project folder
* Create `.env` file based on `.env.example`: `cp .env.example .env` on `Linux/MacOS` or `copy .env.example .env` on `Windows`
* Update the variables inside `.env` with the correct values
* Remember to ask for the `OPENAI_API_KEY` and add it inside your `.env` file.

## 3.1 Run using Python
* Go to your project folder
* Create enviroment `python -m venv venv`, a folder `venv` will be created
* Activate the environment `. venv/bin/activate` for `Linux/MacOS`, or `venv\Scripts\activate` for `Windows`
* Install requirements: `pip install -r requirements.txt`
* Setup `PYTHONPATH` variable `export PYTHONPATH=$(pwd)` for `Linux/MacOS`, or `setx PYTHONPATH "%cd%"` for `Windows`
* Run: `python src/server.py`
* Go to `http://localhost:3000/docs` to access web pages UI

## 3.2 Run using Docker
* Go to your project folder
* Install `docker-compose`. If you installed `Docker Desktop`, you do not have to do this
* Ensure that `.env` file is setup and has correct values
* Build the image: `docker-compose build`
* Run: `docker-compose up` or `docker-compose up -d` for detached run
* Go to `http://localhost:3000/docs` to access web pages UI
* To stop: `docker-compose down`
* Note: `docker-compose` will not watch for file changes, so each time you change some files, you need to run `docker-compose build` again

## 4. Run unit test
* Run unit test with `pytest src/tests`

## 5. Using the API

### With Swagger-UI:
* Go to `http://localhost:3000/docs`, click `Try it out`
* Input your desired `country` and pick your desired `season`. Example: `vietnam` and `spring`
* Click `Excecute` button

### With Terminal/Command Prompt
`
curl -X GET "http://localhost:3000/api/v1/recommendation?country=vietnam&season=spring" -H "accept: application/json"
`
