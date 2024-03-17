from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import cv2 as cv
import os 
from Functions import *

i = 16

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Brain Project API!"}

@app.get("/store/")
async def store():
    global i
    frame_CF = extraction()
    cv.imwrite(f"img/img{i}.jpg", frame_CF)
    i += 1
    return {"message": "Image stored successfully"}

@app.get("/analyze/")
async def analyze_person():
    global i
    frame_AP = extraction()
    cv.imwrite(f"img_analyze/img{i}.jpg", frame_AP)
    lista = data_base_analyze(i)
    os.remove(f"img_analyze/img{i}.jpg")
    i += 1
    return {"lista": lista}

@app.get("/verify/")
async def verify_person():
    index = verify()
    return {"index": index}
