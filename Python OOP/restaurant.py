# restaurant.py

MENU = {
    1: {"name": "Burger", "price": 50.00},
    2: {"name": "Fries", "price": 30.00},
    3: {"name": "Fried Chicken", "price": 80.00},
    4: {"name": "Spaghetti", "price": 60.00},
    5: {"name": "Soda", "price": 25.00}
}

DISCOUNT_RATE = 0.10


def display_welcome_message():
    print("\n" + "*" * 40)
    print(f"{'WELCOME TO FAST FOOD EXPRESS':^40}")
    print("*" * 40)


def display_menu():
    print("\n" + "=" * 40)
    print(f"{'FAST FOOD MENU':^40}")
    print("=" * 40)
    print(f"{'Item #':<8}{'Item Name':<22}{'Price':>10}")
    print("-" * 40)

    for item_id, details in MENU.items():
        print(
            f"{item_id:<8}"
            f"{details['name']:<22}"
            f"P{details['price']:>9.2f}"
        )

    print("=" * 40)


def get_item_choice():
    while True:
        try:
            item_choice = int(
                input("\nEnter the Item Number you want to order: ")
            )

            if item_choice in MENU:
                return item_choice

            print("Invalid item number!")

        except ValueError:
            print("Please enter a valid number.")


def get_quantity(item_choice):
    while True:
        try:
            quantity = int(
                input(
                    f"Enter quantity for "
                    f"{MENU[item_choice]['name']}: "
                )
            )

            if quantity > 0:
                return quantity

            print("Quantity must be at least 1.")

        except ValueError:
            print("Please enter a whole number.")


def add_item_to_order(order_list, item_choice, quantity):
    item = MENU[item_choice]

    item_total = item["price"] * quantity

    order_list.append({
        "name": item["name"],
        "price": item["price"],
        "quantity": quantity,
        "item_total": item_total
    })

    print(
        f"Added {quantity}x {item['name']} "
        f"to your order."
    )


def calculate_order_totals(order_list):
    subtotal = sum(
        item["item_total"]
        for item in order_list
    )

    if subtotal >= 200:
        discount = subtotal * DISCOUNT_RATE
    else:
        discount = 0

    grand_total = subtotal - discount

    return subtotal, discount, grand_total


def print_receipt(order_list):
    subtotal, discount, grand_total = calculate_order_totals(
        order_list
    )

    print("\n" + "=" * 45)
    print(f"{'FAST FOOD EXPRESS RECEIPT':^45}")
    print("=" * 45)

    print(
        f"{'Item':<18}"
        f"{'Qty':<6}"
        f"{'Price':<10}"
        f"{'Total':>11}"
    )

    print("-" * 45)

    for order in order_list:
        print(
            f"{order['name']:<18}"
            f"{order['quantity']:<6}"
            f"P{order['price']:<9.2f}"
            f"P{order['item_total']:>10.2f}"
        )

    print("-" * 45)

    print(f"{'Subtotal:':<34}P{subtotal:>9.2f}")

    if discount > 0:
        print(
            f"{'Discount (10% over P200):':<34}"
            f"-P{discount:>8.2f}"
        )

    print(f"{'GRAND TOTAL:':<34}P{grand_total:>9.2f}")

    print("=" * 45)
    print(f"{'Thank you for dining with us!':^45}")
    print("=" * 45)


def display_exit_message():
    print("\nThank you for visiting! Have a great day!")
