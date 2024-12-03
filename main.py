from fastapi import FastAPI, HTTPException
from math_operations import add, subtract, multiply, divide

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Math API"}

@app.post("/add")
def api_add(a: float, b: float):
    return {"result": add(a, b)}

@app.post("/subtract")
def api_subtract(a: float, b: float):
    return {"result": subtract(a, b)}

@app.post("/multiply")
def api_multiply(a: float, b: float):
    return {"result": multiply(a, b)}

@app.post("/divide")
def api_divide(a: float, b: float):
    try:
        return {"result": divide(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
