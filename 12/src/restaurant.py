from __future__ import annotations

class Coordinates:
    pass

class Employee:
    pass

class Ingredient:
    pass

class Menu:
    def contains(self, ingredient: Ingredient) -> bool:
        return True

class Finances:
    pass

class Dish:
    pass

class RestaurantData:
    pass

class Restaurant:
    def __init__(
            self,
            name: str,
            location: Coordinates,
            employee: list[Employee],
            inventory: list[Ingredient],
            menu: Menu,
            finances: Finances):
        self.name = name
        self.location = location
        self.employee = employee
        self.inventory = inventory
        self.menu = menu
        self.finances = finances

    def transfer_employees(self, employees: list[Employee], restaurant: Restaurant):
        pass

    def order_dish(self, dish: Dish):
        pass

    def add_inventory(self, ingredients: list[Ingredient], cost_in_cents: int):
        pass

    def register_hours_employee_worked(
            self, employee: Employee, minutes_worked: int):
        pass

    def get_restaurant_data(self) -> RestaurantData:
        return RestaurantData()
    
    def change_menu(self, menu: Menu):
        self.menu = menu

    def move_location(self, new_location: Coordinates):
        pass

class GPS:
    def get_coordinates(self) -> Coordinates:
        return Coordinates()

def initialize_gps():
    return GPS()

def schedule_auto_driving_task(location: Coordinates):
    pass

class FoodTruck(Restaurant):
    def __init__(self,
            name: str,
            location: Coordinates,
            employee: list[Employee],
            inventory: list[Ingredient],
            menu: Menu,
            finances: Finances):
        super().__init__(
            name, location, employee, inventory, menu, finances)
        self.__gps = initialize_gps()
        
    def move_location(self, new_location):
        # 次も目的地に向かうためにタスクをスケジューリングする
        schedule_auto_driving_task(new_location)
        return super().move_location(new_location)
    
    def get_current_location(self) -> Coordinates:
        return self.__gps.get_coordinates()
    