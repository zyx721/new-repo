from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import List, Dict
import util

app = FastAPI()

class ImageData(BaseModel):
    image_data: str

@app.post('/classify_image')
def classify_image(image_data: str = Form(...)):
    response = util.classify_image(image_data)
    return response

@app.on_event("startup")
def startup_event():
    print("Starting Python FastAPI Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
