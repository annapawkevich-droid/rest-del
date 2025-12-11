from classes.dish import Dish
from classes.menu import Menu
from classes.customer import Customer
from classes.order import Order
from classes.employee import Employee
from classes.delivery import Delivery
from classes.payment import Payment
from classes.review import Review

# Промокоди
PROMOCODES = {
    "SAVE10": 0.10,
    "SAVE20": 0.20,
    "STUDENT": 0.05
}

def main():
    print("👋 Ласкаво просимо до ресторану!")

    # --- Дані клієнта ---
    name = input("Введіть ваше ім'я: ")
    address = input("Введіть адресу доставки: ")
    phone = input("Введіть номер телефону: ")
    customer = Customer(name, address, phone)

    # --- Меню ---
    menu = Menu()
    menu.add_dish(Dish("Маргарита", 210.5, "Піца"))
    menu.add_dish(Dish("Чізбургер", 170.0, "Бургер"))
    menu.add_dish(Dish("Цезар", 150.0, "Салат"))
    menu.add_dish(Dish("Паста Карбонара", 190.0, "Паста"))

    order = Order(1, customer)

    menu.show_menu()

    # --- Вибір страв ---
    while True:
        choice = input("\nОберіть номер страви (0 — завершити вибір): ")
        if choice == "0":
            break
        dish = menu.get_dish_by_index(int(choice) - 1)
        if dish:
            order.add_dish(dish)
            print(f"✅ Додано {dish.name}")
        else:
            print("❌ Невірний вибір!")

    # --- Промокод ---
    promo = input("Якщо маєте промокод — введіть його (або залиште порожнім): ").upper()
    if promo in PROMOCODES:
        order.discount_rate = PROMOCODES[promo]
        print(f"✅ Промокод прийнято! Ваша знижка {int(PROMOCODES[promo]*100)}%")
    elif promo:
        print("❌ Невірний промокод.")

    # --- Підсумок ---
    order.show_order()

    # --- Оплата ---
    while True:
        pay_method = input("\nОберіть спосіб оплати (готівка / картка): ").strip().lower()
        payment = Payment(pay_method, order.total_price())
        if payment.process_payment():
            break
        else:
            print("🔁 Спробуйте ще раз обрати спосіб оплати.")

    # --- Доставка ---
    courier = Employee("Іван Іванов", "Кур'єр", 18000, 4.8)
    delivery = Delivery(courier, order)
    delivery.show_info()

    # --- Відгук ---
    comment = input("\nЗалиште короткий відгук: ")
    rating = int(input("Оцініть від 1 до 5: "))
    review = Review(customer, rating, comment)
    review.show()

    print("\n🎉 Дякуємо за замовлення!")

if __name__ == "__main__":
    main()
