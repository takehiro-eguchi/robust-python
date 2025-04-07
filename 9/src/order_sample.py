from dataclasses import dataclass

@dataclass(eq=True, order=True)
class NutritionInformation:
    calories: int
    fat: int
    carbohydrates: int

nutritionals = [
    NutritionInformation(calories=100, fat=1, carbohydrates=3),
    NutritionInformation(calories=50, fat=6, carbohydrates=4),
    NutritionInformation(calories=125, fat=12, carbohydrates=3)
]
print(f"ソート前: {nutritionals}")
nutritionals = sorted(nutritionals)
print(f"ソート後: {nutritionals}")
