from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model_noDB import *
app = FastAPI()


hosts = [
    "https://localhost:8000" 
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=hosts, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello, world!"}


@app.post("/api/storing")
def storing():
    pass


@app.post("/api/finding")
def finding():
    pass



@app.post("/api/analisar")
def analisar():
    pass
