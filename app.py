# this is python file to test

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"hello": "Bitfumes"}