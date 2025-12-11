from .dish import Dish

class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def show_menu(self):
        print("\n📋 Меню ресторану:")
        for i, dish in enumerate(self.dishes, 1):
            print(f"{i}. {dish}")

    def get_dish_by_index(self, index):
        if 0 <= index < len(self.dishes):
            return self.dishes[index]
        return None
