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
def read_root():
    return {"message": "Hello, world!"}


@app.get("/api/todo")
async def get_todo():
    return 1

@app.get("/api/todo{id}")
async def get_todo_by_id(id):
    return 1


@app.post("/api/todo")
async def post_todo(todo):
    return 1

@app.update("/api/todo{id}")
async def put_todo(id,  data):
    return 1

@app.delete("/api/todo{id}")
async def delete_todo(todo):
    return 1
