from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Especifique o host como uma lista de origens permitidas
hosts = [
    "https://localhost:8000"  # Você pode adicionar outras origens conforme necessário
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
