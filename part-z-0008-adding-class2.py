from fastapi import FastAPI, Body

app = FastAPI()

AREAS = [
    # {"data_id": "d01", "area": "AI", "lang": "Python", "liked": True, "average_salary": 74_000},
    # {"data_id": "d02", "area": "infrastructure", "lang": "Rust", "liked": True, "average_salary": 99_000},
    # {"data_id": "d03", "area": "Smart Contracts", "lang": "Solidity", "liked": False, "average_salary": 77_000},
    # {"data_id": "d04", "area": "Web", "lang": "JS", "liked": False, "average_salary": 65_000},
    # {"data_id": "d05", "area": "Mobile", "lang": "Kotlin", "liked": True, "average_salary": 87_000},
    # {"data_id": "d06", "area": "Mobile", "lang": "JS", "liked": False, "average_salary": 70_000},
    # {"data_id": "d07", "area": "Smart Contracts", "lang": "Vyper", "liked": True, "average_salary": 84_000},
    # {"data_id": "d08", "area": "Smart Contracts", "lang": "Move", "liked": True, "average_salary": 92_000},
]

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


AREAS.append(AREA("d08", "infrastructure", "Go", True, 68_000))

@app.get("/get-areas")
def get_areas():

    return AREAS

# uv run uvicorn main:app --reload
