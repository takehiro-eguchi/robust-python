# 4. 型制約

型アノテーションで学んだことは序章に過ぎず、型制約テクニックを用いれば更なる制限を課すことができる。

|型制約|説明|
|---|---|
|Optional|None参照を置き換える|
|Union|扱える複数のデータ型|
|Literal|指定できる値をごく一部に制限する|
|Annotated|扱えるデータ型と値の条件を指定する|
|NewType|特定のコンテキスト内だけで扱えるデータ型を作る|
|Final|変数を束縛し変更できないようにする|

# 4.1. Optional型

プログラムをしていると困ったときに無効な値として`None`をreturnしてしまいがち。
ただ、`Optional`を使うことで利用者に`None`が返ってくる可能性を提示することができる。

```python
def get_user_name(id: int) -> Optional[str]:
    users = {
        1: "User1",
        2: "User2"
    }
    return users.get(id, None)

name = get_user_name(1)
print(f"lower name = {name.lower()}")
```

これに対して、`mypy`を実行すると

```
optional.py:11: error: Item "None" of "str | None" has no attribute "lower"  [union-attr]
```

といった具合に

> `None`が返ってくる可能性があるから、考慮しないとだめだよ。

ということを伝えることができる。文字列だとまあこんな感じですが、
`list`の場合などは

* `None`が返る
* 無効値として`空リスト`が返る
* 検索対象が存在しなかったという意味で`空リスト`が返る

などいろいろと悩むポイントはありそうなので、意図を正確に伝える意味でも利用を推奨します。

## 4.2. Union型

型アノテーションの良いところとして、利用する方に制約を付けることができるというものだが、
これはPythonの特性であるダックタイピングの利点と相反するものになってしまう。
そんな時に、`Union`を利用することで、**これとこれはOKだよ**という制約を付けることができるため、型に制約を付け堅牢なプログラミングをしつつ、ダックタイピングの良さも利用することができるいいとこどりの制約と言える。

```python
class Stock:
    def __init__(self):
        self.issueCd = "1301"
        self.name = "極洋"
        self.price = 4510

class Bond:
    def __init__(self):
        self.issueCd = "JGB0172"
        self.name = "利付国庫債券（5年）（第172回）"
        self.price = 100.19
        self.expire_date = date(2029, 6, 20)

class Future:
    def __init__(self):
        self.issueCd = "NK2252412"
        self.name = "日経225先物24年12月"
        self.price = 37723.91
        self.expire_date = date(2024, 12, 13)

# 終了日を取得します
def get_end_date(issue: Union[Bond, Future]) -> date:
    return issue.expire_date

# 銘柄ごとの終了日を取得し、表示します
bond = Bond()
end_date = get_end_date(bond)
print(f"end_date = {end_date}")
future = Future()
end_date = get_end_date(future)
print(f"end_date = {end_date}")
stock = Stock()
end_date = get_end_date(stock)
print(f"end_date = {end_date}")
```

これに`mypy`を実行すると

```ps1
union.py:39: error: Argument 1 to "get_end_date" has incompatible type "Stock"; expected "Bond | Future"  [arg-type]
```

といった具合に警告してくれる。使い時が結構ありそう。

# 4.3. Literal型

`Literal型`を利用することにより、設定される値を制限することができるようになる。
オブジェクト指向になれた人間としては、利用するユースケースがあまり想像できないが、
あまり多様な値を入れたくない場合に利用するとのこと。
個人的に列挙型でよいのでは？とも思ったが、記載によると列挙型より軽量とのこと。
そう考えると活躍の場はありそう。

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class Janken:
    name: Literal["グー", "チョキ", "パー"]

goo = Janken("グー")
print(goo)
press = Janken("プレス機")
print(press)
```

`mypy`の実行結果は

```ps1
literal.py:10: error: Argument 1 to "Janken" has incompatible type "Literal['プレス機']"; expected "Literal['グー', 'チョキ', 'パー']"  [arg-type]
```

## 4.4. Annotated型

`Literal型`は許可する対象が多くなってくると、やや煩雑ですが、これをより柔軟にヒントとして与えることができるようになったものが`Annotated型`です。

```python
from typing import Annotated, Optional
from pydantic import Field

def get_janken_name(id: Annotated[int, Field(ge=1, le=3)]) -> Optional[str]:
    jankens = {
        1:"グー", 2: "チョキ", 3:"パー"
    }
    return jankens.get(id)

name = get_janken_name(1)
print(name)
name = get_janken_name(5)
print(name)
```

しかし、これは`Field`の箇所は評価してくれないようで

```ps1
Success: no issues found in 1 source file
```

通ってしまいました。正直コメントとの差別化はあまりできていないように思われます。
これからの進化に期待でしょうか。

## 4.5. NewType型

既存のクラスから便宜的な新しいクラスを作成することができる。

```python
from typing import NewType

TrimmedStr = NewType("TrimmedStr", str)

def get_word_count(text: TrimmedStr) -> int:
    return len(text)

text = "  aaaa  "
count = get_word_count(text)
print(count)

trimmed_str = TrimmedStr(text.strip())
count = get_word_count(trimmed_str)
print(count)
```

`mypy`を実行すると

```ps1
new_type.py:9: error: Argument 1 to "get_word_count" has incompatible type "str"; expected "TrimmedStr"  [arg-type]
```

こんな感じで警告してくれる。

## 4.6. Final型

これは正直かなり待望でした。pythonは定数が命名規則のみによって提供されていましたが、
これにより、変数の再定義を防ぐことができます。

```python
from typing import Final

class Const:
    PROGRAM: Final = "PYTHON"

Const.PROGRAM = "Java"
print(Const.PROGRAM)
```

```ps1
final.py:6: error: Cannot assign to final attribute "PROGRAM"  [misc]
```

## 4.7. まとめ

型チェッカに従うことありきにはなるが、型制約により品質を上げることができるのは間違いない。
