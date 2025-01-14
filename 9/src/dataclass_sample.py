from copy import deepcopy
from dataclasses import dataclass
import datetime
from enum import Enum, auto

@dataclass
class MyFraction:
    numerator: int = 0  # 分子
    denominator: int = 1    # 分母

# ヤード・ポンド法の単位
class ImperialMeasure(Enum):
    TEASPOON = auto()
    TABLESPOON = auto()
    CUP = auto()

# ブロート
class Broth(Enum):
    VEGETABLE = auto()
    CHICKEN = auto()
    BEEF = auto()
    FISH = auto()

# ブロートに追加される材料（イミュータブル）
@dataclass(frozen=True)
class Ingredient:
    name: str
    amount: float = 1
    units: ImperialMeasure = ImperialMeasure.CUP

@dataclass(eq=True) # 比較ではオブジェクト比較ではなく値比較を行う
class Recipe:
    aromatics: set[Ingredient]  # 香辛料
    broth: Broth
    vegetables: set[Ingredient]
    meats: set[Ingredient]
    starches: set[Ingredient]   # でんぷん質
    garnishes: set[Ingredient]  # 浮き実
    time_to_cook: datetime.timedelta

    # レシピをベジタリアン化する
    def make_vegetarian(self):
        self.meats.clear()  # 肉を削除
        self.broth = Broth.VEGETABLE

    # 材料一覧を取得する
    def get_ingredient_names(self):
        ingredients = (
            self.aromatics
            | self.vegetables
            | self.meats
            | self.starches
            | self.garnishes
        )
        return { ing.name for ing in ingredients } | {
            self.broth.name.capitalize() + " broth"
        }

if __name__ == "__main__":
    pepper = Ingredient("Pepper", 1, ImperialMeasure.TABLESPOON)
    garlic = Ingredient("Garlic", 2, ImperialMeasure.TEASPOON)
    carrots = Ingredient("Carrots", .25, ImperialMeasure.CUP)
    celery = Ingredient("Celery", .25, ImperialMeasure.CUP)
    onions = Ingredient("Onions", .25, ImperialMeasure.CUP)
    parsley = Ingredient("Parsley", 2, ImperialMeasure.TABLESPOON)
    noodles = Ingredient("Noodles", 1.5, ImperialMeasure.CUP)
    chicken = Ingredient("Chicken", 1.5, ImperialMeasure.CUP)
    #chicken.amount = 2.0    # これはエラー

    soup = Recipe(
        aromatics={pepper, garlic},
        broth=Broth.CHICKEN,
        vegetables={celery, onions, carrots},
        meats={chicken},
        starches={noodles},
        garnishes={parsley},
        time_to_cook=datetime.timedelta(minutes=60))
    
    print(f"soup = {soup}")
    
    # ベジタリアン向けにする
    vegetarian_soup = deepcopy(soup)
    print(f"after deepcopy. eq = {soup == vegetarian_soup}")

    vegetarian_soup.make_vegetarian()
    print(f"after make_vegetarian. eq = {soup == vegetarian_soup}")
    vegetarian_ingredients = vegetarian_soup.get_ingredient_names()
    print(f"vegetarian_soup = {vegetarian_ingredients}")
