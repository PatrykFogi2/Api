import Statistics
from fastapi import FastAPI


app = FastAPI()


@app.get("/stats")
async def stats(url: str):
    work = Statistics.get_information(url)
    return work

