# pip install fastapi uvicorn

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def central_function():
    return {"lucifer": "11"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

