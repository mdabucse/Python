from fastapi import FastAPI
app = FastAPI()

@app.get("/latest")
def latest():
    return {"order": "latest"}