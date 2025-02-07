class Capsule:
    def __init__(self):
        self.public_prop = "AAA"
        self._protected_prop = "BBB"
        self.__private_prop = "CCC"
    
    def __repr__(self):
        return f"(repr)public = {self.public_prop}, protected = {self._protected_prop}, private = {self.__private_prop}"

    # def __str__(self):
    #     return f"(str)public = {self.public_prop}, protected = {self._protected_prop}, private = {self.__private_prop}"

capsule = Capsule()
capsule.public_prop = "DDDD"
capsule._protected_prop = "EEEE"
capsule.__private_prop = "FFFF" # エラーにはならないが変更はできない
print(f"capsule : {capsule}")
