from fastapi import FastAPI

app = FastAPI()

AREAS = [
    {"area": "AI", "most_used_lang": "Python", "do I like": True},
    {"area": "infrastructure", "most_used_lang": "Rust", "do I like": True},
    {"area": "Smart Contracts", "most_used_lang": "Solidity", "do I like": False},
    {"area": "Web", "most_used_lang": "JS", "do I like": False},
    {"area": "Mobile", "most_used_lang": "Kotlin", "do I like": True},
]

@app.get("/areas")
def read_areas():
    return AREAS


@app.get("/areas/{searched_area}")
def read_area(searched_area: str):

    for a in AREAS:

        if a.get("area").lower() == searched_area.lower():

            return a 
    
    return {"error": "Not found!"}

# uv run uvicorn main:app --reload
