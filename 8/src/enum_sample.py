from enum import Enum

class MotherSauce(Enum):
    BECHAMEL = "ベシャメル"
    VELOUTE = "ヴローテ"
    ESPAGNOLE = "エスパニョール"
    TOMATO = "トマト"
    HOLLANDAISE = "オランデーズ"

# 個別に表示
print(MotherSauce.BECHAMEL)
print(MotherSauce.HOLLANDAISE.value)

# 全てを表示
for mother_sauce in MotherSauce:
    print(f"{mother_sauce}:{mother_sauce.value}")
