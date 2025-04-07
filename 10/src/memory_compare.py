import tracemalloc
from dataclasses import dataclass
import random

# データクラスの定義
@dataclass
class PersonDataClass:
    name: str
    gender: str
    age: int

# ランダムデータ生成関数
def generate_random_data(num_entries):
    names = ["Alice", "Bob", "Charlie", "David", "Eva"]
    genders = ["Male", "Female"]
    data_list = []
    
    for _ in range(num_entries):
        name = random.choice(names)
        gender = random.choice(genders)
        age = random.randint(1, 100)
        data_list.append((name, gender, age))
    
    return data_list

# 1万件のランダムデータを生成
num_entries = 10000
random_data = generate_random_data(num_entries)

# 辞書のメモリ使用量を測定
tracemalloc.start()
dict_data = [{"name": name, "gender": gender, "age": age} for name, gender, age in random_data]
dict_memory_usage = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

# データクラスのメモリ使用量を測定
tracemalloc.start()
dataclass_data = [PersonDataClass(name, gender, age) for name, gender, age in random_data]
dataclass_memory_usage = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print(f"Memory usage for dictionary: {dict_memory_usage} bytes")
print(f"Memory usage for dataclass: {dataclass_memory_usage} bytes")
