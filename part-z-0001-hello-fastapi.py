from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Subject": "FastAPI is coming..."}

def main():

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
