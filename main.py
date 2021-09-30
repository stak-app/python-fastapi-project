import httpx
from fastapi import FastAPI

app = FastAPI()

URL = "https://www.boredapi.com/api/activity"


async def request(client):
    response = await client.get(URL)
    return response.json()


@app.get("/")
async def root():
    async with httpx.AsyncClient() as client:
        return await request(client)
