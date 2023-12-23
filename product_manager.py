

# product_manager.py
import csv
import os

CSV_FILE = "Tickets.csv"

def read_data():
    data = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
    return data

def write_data(data):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ["name", "count", "price_per_one", "sold"]  # Добавлен новый столбец "sold"
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# def mark_product_as_sold(product_name):
#     data = read_data()
#     breakpoint()
#     found = False
#     for product in data:
#         if product["name"] == product_name:
#             product["sold"] = True
#             found = True
#             break

#     if found:
#         write_data(data)
#         print(f"Товар '{product_name}' отмечен как проданный.")
#     else:
#         print(f"Товар '{product_name}' не найден.")

def add_product_to_db(name, count, price_per_one):
    new_data = read_data()
    new_data.append({"name": name, "count": count, "price_per_one": price_per_one})
    write_data(new_data)
    print(f"Товар '{name}' добавлен в систему.")

def edit_product_in_db(product_name, new_count, new_price_per_one):
    data = read_data()
    found = False
    for product in data:
        if "name" in product and product["name"] == product_name:
            product["count"] = new_count
            product["price_per_one"] = new_price_per_one
            found = True
            break

    if found:
        write_data(data)
        print(f"Товар '{product_name}' отредактирован.")
    else:
        print(f"Товар '{product_name}' не найден.")

    if found:
        write_data(data)
        print(f"Товар '{product_name}' отредактирован.")
    else:
        print(f"Товар '{product_name}' не найден.")

def delete_product_from_db(product_name):
    data = read_data()
    found = False
    for product in data:
        if product["name"] == product_name:
            data.remove(product)
            found = True
            break

    if found:
        write_data(data)
        print(f"Товар '{product_name}' удален.")
    else:
        print(f"Товар '{product_name}' не найден.")

def search_product_in_db(product_name):
    data = read_data()
    found = False
    for product in data:
        if product["name"] == product_name:
            print(f"Найден товар '{product_name}': {product}")
            found = True
    
    if not found:
        print(f"Товар '{product_name}' не найден.")


    # Обновление данных о продуктах в файле

    # for item in cart:
    #     edit_product_in_db(item["name"], item["count"], item["price_per_one"])

sales_history = []
def add_item(cart, item, price, quantity=1):
    cart.append({"item": item, "price": price, "quantity": quantity})
    return cart

def remove_item(cart, item_index):
    if item_index < len(cart):
        removed_item = cart.pop(item_index)
        print(f"Removed {removed_item['quantity']} {removed_item['item']}(s) from the cart.")
    else:
        print("Invalid item index.")
    return cart

def checkout(cart):
    total_amount = sum(item["price"] * item["quantity"] for item in cart)
    print(f"Итоговая сумма продажи: ${total_amount:.2f}")

    apply_discount_option = input("Хотите применить скидку? (yes/no): ").strip().lower()
    if apply_discount_option == "yes":
        discount_percentage = float(input("Введите процент скидки: "))
        total_amount *= (1 - discount_percentage / 100)

    payment_type = input("Выберите тип платежа (cash/card): ").strip().lower()

    if payment_type == "cash":
        payment_amount = float(input("Введите сумму наличными: $"))
        if payment_amount < total_amount:
            print("Недостаточно средств. Продажа отменена.")
            return
    elif payment_type == "card":
        payment_amount = total_amount
    else:
        print("Неверный тип платежа. Продажа отменена.")
        return

    change = payment_amount - total_amount

    # for item in cart:
    #     mark_product_as_sold(item["name"])

    # Добавление информации о продаже в историю
    sale_record: dict = {
        "cart": cart,
        "total_amount": total_amount,
        "discount": discount_percentage if apply_discount_option == "yes" else 0,
        "payment_type": payment_type,
        "payment_amount": payment_amount,
        "change": change
    }

    global sales_history
    sales_history.append(sale_record)
    print("Продажа завершена успешно.")
    print(f"Сдача: ${change:.2f}")


def manage_products():
    cart = []
    
    while True:
        command = input("Введите команду (add_product, edit_product, delete_product, search_product, make_sale, exit): ").strip()

        if command == "add_product":
            product_name = input("Введите название товара: ").strip()
            product_count = int(input("Введите количество товара: "))
            product_price = float(input("Введите цену товара за штуку: "))
            add_product_to_db(product_name, product_count, product_price)

        elif command == "edit_product":
            product_name = input("Введите название товара для редактирования: ").strip()
            new_count = int(input("Введите новое количество товара: "))
            new_price_per_one = float(input("Введите новую цену товара за штуку: "))
            edit_product_in_db(product_name, new_count, new_price_per_one)

        elif command == "delete_product":
            product_name = input("Введите название товара для удаления: ").strip()
            delete_product_from_db(product_name)

        elif command == "search_product":
            product_name = input("Введите название товара для поиска: ").strip()
            search_product_in_db(product_name)

        elif command == "make_sale":
            print("\n1. Add item\n2. Remove item\n3. Checkout\n4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                item = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter quantity: "))
                cart = add_item(cart, item, price, quantity)
            elif choice == "2":
                index = int(input("Enter item index to remove: "))
                cart = remove_item(cart, index)
            elif choice == "3":
                checkout(cart)
                break
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

        # make_sale(cart)

        elif command == "exit":
            print("Выход из программы.")
            break

        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    manage_products()

# product_manager.py
