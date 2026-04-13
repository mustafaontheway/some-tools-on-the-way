from fastapi import FastAPI, Body

from pydantic import BaseModel, Field

app = FastAPI()

class AREA(BaseModel):
  
    data_id: str = Field(min_length=3, max_length=8)
    area: str = Field(min_length=2)
    lang: str = Field(min_length=2)
    liked: bool = Field(default = False, description = "Do you like the area?")
    average_salary: int = Field(gt=0, lt= 500_000)


AREAS = [
    AREA(data_id="d01", area="AI", lang="Python", liked=True, average_salary=74_000),
    AREA(data_id="d02", area="infrastructure", lang="Rust", liked=True, average_salary=99_000),
    AREA(data_id="d03", area="Smart Contracts", lang="Solidity", liked=False, average_salary=77_000),
    AREA(data_id="d04", area="Web", lang="JS", liked=False, average_salary=65_000),
    AREA(data_id="d05", area="Mobile", lang="Kotlin", liked=True, average_salary=87_000),
    AREA(data_id="d06", area="Mobile", lang="JS", liked=False, average_salary=70_000),
    AREA(data_id="d07", area="Smart Contracts", lang="Vyper", liked=True, average_salary=84_000),
    AREA(data_id="d08", area="Smart Contracts", lang="Move", liked=True, average_salary=92_000),
]



# uv run uvicorn main:app --reload
