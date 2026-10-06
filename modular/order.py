# order.py

from food import MENU


def get_item_choice():
    """Gets a valid item number from the customer."""

    while True:
        try:
            item_choice = int(
                input("\nEnter the Item Number you want to order: ")
            )

            if item_choice not in MENU:
                print(
                    "Invalid item number! "
                    "Please pick an item from the menu."
                )
                continue

            return item_choice

        except ValueError:
            print(
                "Invalid input! "
                "Please enter a valid numerical Item Number."
            )


def get_quantity(item_choice):
    """Gets a valid quantity from the customer."""

    while True:
        try:
            quantity = int(
                input(
                    f"Enter quantity for "
                    f"{MENU[item_choice]['name']}: "
                )
            )

            if quantity <= 0:
                print("Quantity must be at least 1.")
                continue

            return quantity

        except ValueError:
            print(
                "Invalid input! "
                "Quantity must be a whole number."
            )


def add_item_to_order(order_list, item_choice, quantity):
    """Adds an item to the customer's order."""

    item_data = MENU[item_choice]

    item_total = item_data["price"] * quantity

    order_list.append({
        "name": item_data["name"],
        "price": item_data["price"],
        "quantity": quantity,
        "item_total": item_total
    })

    print(
        f"Added {quantity}x "
        f"{item_data['name']} to your order."
    )


def ask_for_another_item():
    """Asks if the customer wants another item."""

    while True:
        another = input(
            "\nWould you like to order another item? (yes/no): "
        ).strip().lower()

        if another in ["yes", "y"]:
            return True

        elif another in ["no", "n"]:
            return False

        else:
            print(
                "Invalid response. "
                "Please enter 'yes' or 'no'."
            )
