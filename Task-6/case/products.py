from fastapi import FastAPI
app = FastAPI()

@app.get("/{id}")
def product(id: int):
    return {"id": id, "name": "Phone"}