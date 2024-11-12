from typing import TypedDict

class Range(TypedDict):
    min: float
    max: float

range1: Range = {
    'min': 1.2,
    'max': 4.5
}

print(f"range1 = {range1}")

range2: Range = {
    'min': 1.2,
    'max': 4
}

print(f"range2 = {range2}")
