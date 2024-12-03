from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  # Importing BaseModel for request body validation
from math_operations import add, subtract, multiply, divide

app = FastAPI()

# Define a Pydantic model for request body
class MathRequest(BaseModel):
    a: float
    b: float

@app.get("/")
def root():
    return {"message": "Welcome to the Math API"}

@app.post("/add")
def api_add(request: MathRequest):  # Using the MathRequest model
    return {"result": add(request.a, request.b)}

@app.post("/subtract")
def api_subtract(request: MathRequest):  # Using the MathRequest model
    return {"result": subtract(request.a, request.b)}

@app.post("/multiply")
def api_multiply(request: MathRequest):  # Using the MathRequest model
    return {"result": multiply(request.a, request.b)}

@app.post("/divide")
def api_divide(request: MathRequest):  # Using the MathRequest model
    try:
        return {"result": divide(request.a, request.b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
