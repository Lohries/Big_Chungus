from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import cv2 as cv
import os 
from Functions import *

app = FastAPI()
i = 0
class Data(BaseModel):
    name: str
    age: int
    gender: str
    race: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Brain Project API!"}

@app.post("/store/")
async def store():
        
        frame_CF = extraction(i)
        cv.imwrite("img/img.jpg", frame_CF)

@app.post("/analyze/")
async def analyze_person(data: Data):
    frame_CF = extraction(0)
    cv.imwrite("img_analyze/img.jpg", frame_CF)
    index = data_base_analyze("img_analyze/img.jpg")
    os.remove("img_analyze/img.jpg")
    return {"index": index}

@app.post("/verify/")
async def verify_person(file: UploadFile = File(...)):
    with open("img_find/img.jpg", "wb") as f:
        f.write(file.file.read())
    
    index = verify()
    return {"index": index}
