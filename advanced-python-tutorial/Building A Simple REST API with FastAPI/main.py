# pip install fastapi
# pip install uvcorn
# pip install pydantic
# run: uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {"hello": "world"}

@app.post('/')
def hello_post():
    return {"success": "you posted!"}

@app.get('/something')
def something():
    return {"data": "something"}