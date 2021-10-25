from fastapi import FastAPI

app = FastAPI()

@app.get(
    "/hello",
    summary="Hello World",
)
async def hello_world(
):
    return {
        "message": "Hello, World"
    }

