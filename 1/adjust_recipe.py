from fractions import Fraction

class Recipe:
    """
    レシピを表すクラスです。料理名と材料ごとの量を保持しています。
    """
    def __init__(self, servings, ingredients):
        self.servings = servings
        self.ingredients = ingredients

    def get_ingredients(self):
        return self.ingredients
    
    def clear_ingredients(self):
        self.ingredients = list([])

    def __str__(self):
        ingredients_str = ",".join([f"({ingredient.__str__()})" for ingredient in self.ingredients])
        return f"servings={self.servings}, ingredients=[{ingredients_str}]"

class Ingredient:
    """
    材料を表すクラスです。材料ごとに必要な量を保持しています。
    """
    
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def adjust_proportation(self, rate):
        """
        与えられた比率をもとに量を調整します。
        """
        self.quantity *= rate

    def __str__(self):
        return f"name={self.name}, quantity={self.quantity}"


def adjust_recipe(recipe, servings):
    """
    料理のレシピを取り、材料の量を調整して、提供できる人数を変える
    :param recipe: 調整が必要なRecipe
    :param servings: 提供人数
    :return Recipe: 新しい提供人数に合わせて、人数と材料の量を調整したレシピ
    """
    # 材料データのコピーを作る
    new_ingredients = list(recipe.get_ingredients())
    recipe.clear_ingredients()
    for ingredient in new_ingredients:
        # Fractionを用いて、提供人数 / レシピ上の提供人数 を計算する
        ingredient.adjust_proportation(Fraction(servings, recipe.servings))

    # 調整後のレシピを返す
    return Recipe(servings, new_ingredients)

if __name__ == "__main__":
    # 元々のレシピを作成
    ingredients = [ Ingredient("Sugar", 200), Ingredient("Salt", 100), Ingredient("Milk", 500)]
    recipe = Recipe(3, ingredients)

    # 12人分に調整する
    new_recipe = adjust_recipe(recipe, 12)
    print(new_recipe)