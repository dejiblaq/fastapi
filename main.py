from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def post():
    return {"message": "Hello from the post route"}

@app.put("/")
async def put():
    return {"message": "Hello from the put route"}
    