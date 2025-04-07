from dataclasses import dataclass

dict_person = {
    "name": "",
    "years_experience": 0,
    "address": ""
}

@dataclass
class PersonDC:
    name: str = ""
    years_experience: int = 0
    address: str = ""

class Person:
    def __init__(this, name: str, years_experience: int, address: str):
        this.name = name
        this.years_experience = years_experience
        this.address = address

    def __repr__(this):
        return f"name = {this.name}, years_experience = {this.years_experience}, address = {this.address}"

person = Person("", 0, "")
print(f"person = {person}")
