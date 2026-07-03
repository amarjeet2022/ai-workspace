from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hellow world"}

@app.get("/user")
def user():
    return [
        {"id": 1, "name": "Amarjeet"},
        {"id": 2, "name": "Aman"},

    ]