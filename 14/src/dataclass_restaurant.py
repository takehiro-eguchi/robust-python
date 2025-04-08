from typing import Literal, Optional, Union
from pydantic.dataclasses import dataclass
import yaml

@dataclass
class AccountAndRoutingNumber:
    account_number: str
    routing_number: str

@dataclass
class BankDetails:
    bank_details: AccountAndRoutingNumber

AddressOrBankDetails = Union[str, BankDetails]

Position = Literal["Chef", "Sous Chef", "Host", "Server", "Delivery Driver"]

    # position: Chef
    # position: Server
    # position: Sous Chef
    # position: Host

@dataclass
class Dish:
    name: str
    price_in_cents: int
    description: str
    picture: Optional[str] = None

@dataclass
class Employee:
    name: str
    position: Position
    payment_details: AddressOrBankDetails

@dataclass
class Restaurant:
    name: str
    owner: str
    address: str
    employees: list[Employee]
    dishes: list[Dish]
    number_of_seats: int
    to_go: bool
    delivery: bool

def load_restaurant(filename: str) -> Restaurant:
    with open(filename) as yaml_file:
        data = yaml.safe_load(yaml_file)
        return Restaurant(**data)
    
restaurant = load_restaurant("restaurant.yaml")
print(f"restaurant = {restaurant}")
