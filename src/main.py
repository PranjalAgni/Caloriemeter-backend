# main.py

from fastapi import FastAPI, UploadFile
import os
import aiofiles
from uuid import uuid4
from starlette.background import BackgroundTasks
from src.prediction import predict_food_item, remove_file

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Fast API is running 🚀"}


@app.post("/predict")
async def predict_items(input: UploadFile, background_tasks: BackgroundTasks):
    input_image_id = str(uuid4())[:4]
    input_image_filename_extension = input.filename.split(".")
    input_image_filename = f"{input_image_filename_extension[0]}_{input_image_id}.{input_image_filename_extension[1]}"
    input_image_location = os.path.abspath(
        os.path.join("src", "images", input_image_filename)
    )
    print(f"This is storage location {input_image_location}")
    async with aiofiles.open(input_image_location, "wb") as out_file:
        content = await input.read()  # async read
        await out_file.write(content)  # async write

    predicted_food_item = predict_food_item(input_image_location)
    background_tasks.add_task(remove_file, input_image_location)
    return {"itemName": input.filename, "result": predicted_food_item}
