from fastapi import FastAPI

app = FastAPI()

REC = [
    'Eat Vietnamese Pho',
    'Go camping in Ba Vi',
    'Have Picnic in Moc Chau'
]

@app.get("/recommendation")
async def get_recommendation(country: str, season: str):
    return REC