from fastapi import FastAPI
import uvicorn

app = FastAPI()

AREAS = [
    {"area": "AI", "most_used_lang": "Python", "do I like": True},
    {"area": "infrastructure", "most_used_lang": "Rust", "do I like": True},
    {"area": "Smart Contracts", "most_used_lang": "Solidity", "do I like": False},
    {"area": "Web", "most_used_lang": "JS", "do I like": False},
    {"area": "Mobile", "most_used_lang": "Kotlin", "do I like": True},
]

def main():

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

@app.get("/areas")
def read_areas():
    return AREAS


@app.get("/areas/{area}")
def read_area(area: str):

    for area in AREAS:

        if area.get("area").lower() == area.lower():

            return area
          

if __name__ == "__main__":
    main()


# uv run uvicorn main:app --reload
