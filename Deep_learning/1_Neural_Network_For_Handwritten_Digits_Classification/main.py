from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import numpy as np
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define the model architecture
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(10, activation='softmax')
])

# Load the model weights
model.load_weights('model.h5')


# Define the FastAPI app
app = FastAPI()

# Serve static files (like HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the input data model
class Item(BaseModel):
    data: list

# Define a prediction endpoint
@app.post("/predict/")
async def predict(item: Item):
    input_data = np.array(item.data).reshape(1, 28, 28)
    prediction = model.predict(input_data)
    return {"prediction": prediction.tolist()}

# Route for serving the HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)
