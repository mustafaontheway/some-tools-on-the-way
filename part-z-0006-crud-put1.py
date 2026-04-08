from fastapi import FastAPI, Body

app = FastAPI()

AREAS = [
    {"data_id": "d01", "area": "AI", "one_of_most_used_langs": "Python", "do I like": True},
    {"data_id": "d02", "area": "infrastructure", "one_of_most_used_langs": "Rust", "do I like": True},
    {"data_id": "d03", "area": "Smart Contracts", "one_of_most_used_langs": "Solidity", "do I like": False},
    {"data_id": "d04", "area": "Web", "one_of_most_used_langs": "JS", "do I like": False},
    {"data_id": "d05", "area": "Mobile", "one_of_most_used_langs": "Kotlin", "do I like": False},
    {"data_id": "d06", "area": "Mobile", "one_of_most_used_langs": "Dart", "do I like": True},
    {"data_id": "d07", "area": "Smart Contracts", "one_of_most_used_langs": "Vyper", "do I like": True},
    {"data_id": "d08", "area": "Smart Contracts", "one_of_most_used_langs": "Move", "do I like": True},
]

@app.get("/areas")
def read_areas():
    return AREAS


@app.put("/areas/update-area")
def update_area(ua: dict = Body()):

    for i in range(len(AREAS)):

        if AREAS[i].get("data_id").lower() == ua.get("data_id").lower():

            AREAS[i] = ua


@app.post("/areas-new-area")
def create_new_area(na: dict = Body()):
    AREAS.append(na)

@app.get("/areas-queried-like-condition")
def read_liked_or_disliked_areas_by_query(qa: str, l: bool):

    liked_or_disliked = []

    for a in AREAS:

        if a.get("area").lower() == qa.lower() and a.get("do I like") == l:

            liked_or_disliked.append(a)

    return liked_or_disliked


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
