from fastapi import FastAPI

app = FastAPI()

# fastapi dev main.py

@app.get("/")
async def root():
    return {"message": "Hello World"}