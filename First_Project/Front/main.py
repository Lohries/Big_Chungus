from fastapi import FastAPI
from typing import Union
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>

        <head>
            <title>Deep_Smile</title>
        </head>
        <body>
            <h1>Bem-Vindo</h1>
        </body>
    </html>
    """

