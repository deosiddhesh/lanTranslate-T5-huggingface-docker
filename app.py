from fastapi import FastAPI
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-base")

app = FastAPI()


@app.get('/')
def home():
    return {"hello": "Bitfumes"}


@app.get('/ask')
def ask(prompt: str):
    result = pipe(prompt)
    return result[0]