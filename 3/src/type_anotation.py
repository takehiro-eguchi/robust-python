def add(value1: int, value2: int) -> int:
    return value1 + value2

# これは実行できるし ->　3
result:int = add(1, 2)
print(f"result = {result}")
# これも実行できる -> "AABB"
result = add("AA", "BB")
print(f"result = {result}")