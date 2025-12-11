import random

class Delivery:
    def __init__(self, courier, order):
        self.courier = courier
        self.order = order
        self.status = "У дорозі"
        self.time = f"{random.randint(20, 45)} хв"

    def show_info(self):
        print(f"🚗 Кур'єр: {self.courier.name}, час доставки: {self.time}")
