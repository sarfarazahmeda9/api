from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/sarfaraz/add")
def add(x:int,y:int):
    return {"result": x + y}

class subtractmodel(BaseModel):
    a: int
    b: int


def subtract(a:int,b:int):
    return a-b

@app.post("/sarfaraz/subtract")
def subtract_numbers(model: subtractmodel):
    return subtract(model.a, model.b)


def multiply(a:int,b:int):
    return a*b

@app.post("/sarfaraz/multiply")
def multiply_numbers(model: subtractmodel):
    return multiply(model.a, model.b)


if __name__ == "__main__":
    print(add(1, 2))

