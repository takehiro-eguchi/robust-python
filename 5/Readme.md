# 5. コレクション型

## コレクション型にも型アノテーションが利用できる

```python
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Cookbook:
    author: str

def create_author_count_mapping(cookbooks: list) -> dict[str, int]:
    counter: dict[str, int] = defaultdict(int)
    for book in cookbooks:
        counter[book.author] += 1
    return counter

# メイン処理
book_counter = create_author_count_mapping(
    [Cookbook("aa"), 
     Cookbook("bb"),
     Cookbook("aa")])
print(f"counter={book_counter}")
```

## 同種コレクションと異種コレクション

