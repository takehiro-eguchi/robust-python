from enum import auto, Enum

class MotherSauce(Enum):
    '''
    auto()メソッドの生成メソッド、定義しない場合は 1,2,3,4 とインクリメントされる
    '''
    def _generate_next_value_(name, start, count, last_values):
        return name.capitalize()

    BECHAMEL = auto()
    VELOUTE = auto()
    ESPAGNOLE = auto()
    TOMATO = auto()
    HOLLANDAISE = auto()

for sauce in MotherSauce:
    print(f"{sauce}:{sauce.value}")
    