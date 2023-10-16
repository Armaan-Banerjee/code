from fastapi import FastAPI

app = FastAPI(title=" A simple pagination learning exercise",
              debug=True)


@app.get(path="/api/hello", name="hello endpoint")
async def hello():
    return {"exercise": "pagination"}
