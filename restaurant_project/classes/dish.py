class Dish:
    def __init__(self, name, price, category, available=True):
        self.name = name
        self.price = price
        self.category = category
        self.available = available

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price} грн"
