from pathlib import Path

from  fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def home():
#     return {"data":"testing"}
#
# @app.get("/about")
# def about():
#     return {"data"}

inventory = {
    1:{
        "name":"milk",
        "price":3.99,
        "brand":"regular"
    }
}
@app.get("/get-item/{item_id}")
def get_item(item_id:int):
    return inventory[item_id]