from __future__ import annotations
from typing import Protocol
import math

class BLTSandwitch:
    def __init__(self):
        self.cost = 6.95
        self.name = "BLT"

    def split_in_half(self) -> tuple[BLTSandwitch, BLTSandwitch]:
        '''
        サンドイッチを半分に分割する方法
        斜めに切る、別々に包むなど
        ２個のサンドイッチを返す
        '''

        return BLTSandwitch(), BLTSandwitch()

class Chili:
    def __init__(self):
        self.cost = 4.95
        self.name = "チリコンカン"

    def split_in_half(self) -> tuple[Chili, Chili]:
        '''
        チリコンカンを半分に分割する方法
        別の容器によそい、とピングを追加する
        ２個のチリコンカンをよそった小鉢を返す
        '''
        return Chili(), Chili()
    
class BaconCheeseBurger:
    def __init__(self):
        self.cost = 11.95
        self.name = "ベーコンチーズバーガー"

class Splittable(Protocol):
    cost: float
    name: str

    def split_in_half(self) -> tuple[Splittable, Splittable]:
        '''
        実装不要
        '''

def split_dish(dish: Splittable) -> tuple[Splittable, Splittable]:
    dishes = dish.split_in_half()
    assert len(dishes) == 2
    for half_dish in dishes:
        half_dish.cost = math.ceil(half_dish.cost) / 2
        half_dish.name = "1/2 " + half_dish.name
    return dishes

if __name__ == "__main__":
    sandwitches = split_dish(BLTSandwitch())
    

