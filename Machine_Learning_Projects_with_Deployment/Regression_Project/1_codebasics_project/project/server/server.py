from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the data model for prediction requests
class PredictRequest(BaseModel):
    total_sqft: float
    location: str
    bhk: int
    bath: int

# Sample data or model simulation
locations_data = ["Location1", "Location2", "Location3"]

def get_location_names() -> List[str]:
    # This function should return the list of location names available
    return locations_data

def get_estimated_price(location: str, total_sqft: float, bhk: int, bath: int) -> float:
    # This is a placeholder function. Replace this logic with your actual model's prediction logic.
    base_price_per_sqft = 5000  # Just an example rate
    estimated_price = total_sqft * base_price_per_sqft
    return estimated_price

@app.get("/get_location_names", response_model=List[str])
def fetch_location_names():
    try:
        locations = get_location_names()
        return locations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict_home_price")
def predict_home_price(request: PredictRequest):
    try:
        estimated_price = get_estimated_price(
            request.location, request.total_sqft, request.bhk, request.bath
        )
        return {"estimated_price": estimated_price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("Starting Python FastAPI Server For Home Price Prediction...")
    # If you have any initialization code, you can add it here
    uvicorn.run(app, host="0.0.0.0", port=8000)
