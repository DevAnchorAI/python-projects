from fastapi import FastAPI
import logging;

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
def home():
    logging.info("Inside Defalt API")
    return {"message": "Hello World"}

@app.get("/greeting/{name}")
def greeting(name:str):
    logging.info("Inside greeting API")
    return "HELLO:"+name;