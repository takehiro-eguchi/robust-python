from typing import TypeVar

T = TypeVar("T")

def reverse(collection: list[T]) -> list[T]:
    return collection[::-1]

col1: list[int] = [1, 2, 3]
print(f"col1 = {col1}")
col2: list[int] = reverse(col1)
print(f"col2 = {col2}")
