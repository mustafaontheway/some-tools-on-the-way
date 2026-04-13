from fastapi import FastAPI, Body

app = FastAPI()

class AREA:
    data_id: str
    area: str
    lang: str
    liked: bool
    average_salary: int

    def __init__(self, data_id, area, lang, liked, average_salary):

        self.data_id = data_id
        self.area = area
        self.lang = lang
        self.liked = liked
        self.average_salary = average_salary

AREAS = [
    AREA("d01", "AI", "Python", True, 74_000),
    AREA("d02", "infrastructure", "Rust", True, 99_000),
    AREA("d03", "Smart Contracts", "Solidity", False, 77_000),
    AREA("d04", "Web", "JS", False, 65_000),
    AREA("d05", "Mobile", "Kotlin", True, 87_000),
    AREA("d06", "Mobile", "JS", False, 70_000),
    AREA("d07", "Smart Contracts", "Vyper", True, 84_000),
    AREA("d08", "Smart Contracts", "Move", True, 92_000),
]

AREAS.append(AREA("d09", "infrastructure", "Go", True, 68_000))

@app.get("/get-areas")
def get_areas():

    return AREAS


@app.post("/add-area")
def add_area(request_new_area = Body()):

    AREAS.append(request_new_area)

# uv run uvicorn main:app --reload
