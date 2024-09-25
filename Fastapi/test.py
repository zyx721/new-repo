from fastapi import FastAPI
from fastapi import Query

app = FastAPI()

@app.get('/blog')
def read_hey(limit: int = Query(...)):  # Specify the type and set a default
    return {"message": limit}
