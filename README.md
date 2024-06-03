# Travel-recommendation-L2

## Setup steps and run

## 1. Setup the project directory
* Download `Docker Desktop`, recommend version `4.29.0`, check Docker release note `https://docs.docker.com/desktop/release-notes/` for versions.
* Download `python` version `3.9.5` (recommend version: `3.8.8 to 3.9.5`) if you do not want to run project with Docker
* Clone the repository `git clone https://github.com/HoangVietPW26/travel_recommedation_L2`.
* Go to your project folder `cd travel_recommendation_L2`, you should see `src` folder if you are at correct place.

## 2. Setup environment variables
* Go to your project folder, you should see `src` folder if you are at correct place.
* Create `.env` with variables file based on `.env.example`
* Update the variables inside `.env` with the correct values
* Remember to ask for the `OPENAI_API_KEY` and add it inside your `.env` file.

## 3.1 Run using Python
* Go to your project folder,, you should see `src` folder if you are at correct place.
* Create enviroment `python -m venv venv`, a folder `venv` will be created
* Activate the environment:
    - `. venv/bin/activate` for `Linux/MacOS`.
    - For `Windows`, recommend `Unix Like Command Shell` like `Git Bash` instead of `Powershell`. Run `. venv/Scripts/activate`
    - From now on, if you run project on `Windows` the instruction assume you use `Git Bash` or `Unix Like Command Shell`
* Install requirements: 
    - `pip install -r requirements.txt` for `Linux/MacOS`. 
    - For `Windows`, comment `uvloop==0.19.0` in  `requirements.txt` file before run `pip install -r requirements.txt`.
* Setup `PYTHONPATH` variable `export PYTHONPATH=$(pwd)`.
* Run: `python server.py`
* Go to `http://localhost:3000/docs` to access web pages UI

## 3.2 Run using Docker
* Go to your project folder `cd travel_recommendation_L2`, you should see `src` folder if you are at correct place.
* Install `docker-compose`. If you installed `Docker Desktop` above, you do not have to do this
* Ensure that `.env` file is setup and has correct values
* Build the image: `docker-compose build`
* Run: `docker-compose up` or `docker-compose up -d` for detached run
* Go to `http://localhost:3000/docs` to access web pages UI
* To stop: `docker-compose down`
* Note: `docker-compose` will not watch for file changes, so each time you change some files, you need to run `docker-compose build` again

## 3.3 Run using Makefile
* Go to your project folder `cd travel_recommendation_L2`, you should see `makefile` file if you are at correct place.
* Install `docker-compose`. If you installed `Docker Desktop` above, you do not have to do this
* Ensure that `.env` file is setup and has correct values
* Build the image: `make build`
* Run: `make up` for detached run
* Go to `http://localhost:3000/docs` to access web pages UI
* To stop: `make down`

## 4. Run unit test
* Go to your project folder, , you should see `src` folder if you are at correct place.
* Remember to activate the environment like in step 3.1
* Setup `PYTHONPATH` variable `export PYTHONPATH=$(pwd)`
* Run unit test with `pytest tests` or `make test`

## 5. Using the API

### With Swagger-UI:
* Go to `http://localhost:3000/docs`, click `Try it out`
* Input your desired `country` and pick your desired `season`. Example: `vietnam` and `spring`
* Click `Excecute` button

### With Terminal/Command Prompt
Run
`
curl -X GET "http://localhost:3000/api/v1/recommendation?country=vietnam&season=spring" -H "accept: application/json"
`
