from dataclasses import dataclass
from typing import Literal

@dataclass
class Janken:
    name: Literal["グー", "チョキ", "パー"]

goo = Janken("グー")
print(goo)
press = Janken("プレス機")
print(press)