from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #Secure form


app = FastAPI()

host = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware, 
    allow_origin = host,
    allow_credential = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)