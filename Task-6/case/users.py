from fastapi import FastAPI
app = FastAPI()

@app.get("/profile")
def profile():
    return {"user": "Abu"}