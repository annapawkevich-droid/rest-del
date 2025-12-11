import random

class Payment:
    def __init__(self, method, amount):
        self.method = method
        self.amount = amount
        self.success = False

    def process_payment(self):
        method = self.method.lower()

        if method == "готівка":
            print(f"💵 Оплата на місці. До сплати: {self.amount:.2f} грн.")
            self.success = True  # оплата пізніше, але замовлення приймається

        elif method == "картка":
            print("💳 Обробка платежу...")
            self.success = random.choice([True, False])
            if self.success:
                print(f"✅ Оплата карткою успішна! Сума: {self.amount:.2f} грн списано.")
            else:
                print("❌ Помилка під час оплати карткою. Спробуйте ще раз.")

        else:
            print("⚠️ Невідомий спосіб оплати.")
            self.success = False

        return self.success
