# main.py

from restaurant import (
    display_welcome_message,
    display_menu,
    display_exit_message,
    get_item_choice,
    get_quantity,
    add_item_to_order,
    print_receipt
)


def ask_to_order():
    while True:
        choice = input(
            "Would you like to place an order? (yes/no): "
        ).strip().lower()

        if choice in ["yes", "y"]:
            return True

        if choice in ["no", "n"]:
            return False

        print("Invalid response. Please enter yes or no.")


def ask_for_another_item():
    while True:
        choice = input(
            "\nWould you like to order another item? (yes/no): "
        ).strip().lower()

        if choice in ["yes", "y"]:
            return True

        if choice in ["no", "n"]:
            return False

        print("Invalid response. Please enter yes or no.")


def run_ordering_system():

    display_welcome_message()

    if not ask_to_order():
        display_exit_message()
        return

    order_list = []

    while True:

        display_menu()

        item_choice = get_item_choice()

        quantity = get_quantity(item_choice)

        add_item_to_order(
            order_list,
            item_choice,
            quantity
        )

        if not ask_for_another_item():
            break

    print_receipt(order_list)


if __name__ == "__main__":
    run_ordering_system()
