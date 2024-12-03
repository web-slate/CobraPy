from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    # Testing the root endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Math API"}

def test_add():
    # Testing the addition operation
    response = client.post("/add", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_subtract():
    # Testing the subtraction operation
    response = client.post("/subtract", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_multiply():
    # Testing the multiplication operation
    response = client.post("/multiply", json={"a": 7, "b": 6})
    assert response.status_code == 200
    assert response.json() == {"result": 42}

def test_divide_success():
    # Testing the division operation (success)
    response = client.post("/divide", json={"a": 20, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 4}

def test_divide_by_zero():
    # Testing division by zero
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero."}
