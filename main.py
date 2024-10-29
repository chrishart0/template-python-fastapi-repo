from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from settings import settings
from loguru import logger

app = FastAPI()

# Configure logger
logger.add("file_{time}.log", rotation="1 day", retention="7 days", level="INFO")


class HelloWorld(BaseModel):
    message: str


def create_hello_world(message: str) -> HelloWorld:
    hello_world = HelloWorld(message=message)
    logger.info(hello_world)
    return hello_world


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    return base**exponent


@app.get("/hello", response_model=HelloWorld)
def hello_world_endpoint():
    return create_hello_world("Hello, world!")


@app.get("/add")
def add_endpoint(a: float, b: float):
    return {"result": add(a, b)}


@app.get("/subtract")
def subtract_endpoint(a: float, b: float):
    return {"result": subtract(a, b)}


@app.get("/multiply")
def multiply_endpoint(a: float, b: float):
    return {"result": multiply(a, b)}


@app.get("/divide")
def divide_endpoint(a: float, b: float):
    try:
        return {"result": divide(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/power")
def power_endpoint(base: float, exponent: float):
    return {"result": power(base, exponent)}


# Example usage
create_hello_world("Hello, world!")
logger.info(add(1, 2))
logger.info(subtract(5, 3))
logger.info(multiply(4, 2))
logger.info(divide(10, 2))
logger.info(power(2, 3))

# Use the loaded settings
logger.info(f"API_KEY: {settings.API_KEY}")
logger.info(f"DATABASE_URL: {settings.DATABASE_URL}")
