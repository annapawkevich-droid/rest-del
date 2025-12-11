import random

class Order:
    def __init__(self, number, customer, discount_rate=0):
        self.number = number
        self.customer = customer
        self.dishes = []
        self.discount_rate = discount_rate

    def add_dish(self, dish):
        self.dishes.append(dish)

    def total_price(self):
        total = sum(d.price for d in self.dishes)
        if self.discount_rate > 0:
            total *= (1 - self.discount_rate)
        return total

    def random_bonus_discount(self):
        bonus = random.choice([0, 0.05, 0.1, 0.15])
        if bonus:
            print(f"🎁 Вам випала бонусна знижка {int(bonus*100)}%!")
            self.discount_rate += bonus

    def show_order(self):
        print(f"\nЗамовлення №{self.number}:")
        for d in self.dishes:
            print(f" - {d.name} ({d.price} грн)")
        print(f"Загальна сума: {self.total_price():.2f} грн")
