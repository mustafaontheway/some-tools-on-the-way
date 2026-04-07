from fastapi import FastAPI

app = FastAPI()

AREAS = [
    {"area": "AI", "one_of_most_used_langs": "Python", "do I like": True},
    {"area": "infrastructure", "one_of_most_used_langs": "Rust", "do I like": True},
    {"area": "Smart Contracts", "one_of_most_used_langs": "Solidity", "do I like": False},
    {"area": "Web", "one_of_most_used_langs": "JS", "do I like": False},
    {"area": "Mobile", "one_of_most_used_langs": "Kotlin", "do I like": False},
    {"area": "Mobile", "one_of_most_used_langs": "Dart", "do I like": True},
    {"area": "Smart Contracts", "one_of_most_used_langs": "Vyper", "do I like": True},
    {"area": "Smart Contracts", "one_of_most_used_langs": "Move", "do I like": True},
]

@app.get("/areas")
def read_areas():
    return AREAS


@app.get("/areas-queried")
def read_areas_by_query(qa: str):

    q = []

    for a in AREAS:

        if a.get("area").lower() == qa.lower():

            q.append(a)
    
    return q


@app.get("/areas/{searched_area}")
def read_area(searched_area: str):

    for a in AREAS:

        if a.get("area").lower() == searched_area.lower():

            return a 
    
    return {"error": "Not found!"}

# uv run uvicorn main:app --reload
