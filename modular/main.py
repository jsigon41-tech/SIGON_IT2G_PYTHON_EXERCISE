# main.py

from food import display_menu
from order import (
    get_item_choice,
    get_quantity,
    add_item_to_order,
    ask_for_another_item
)
from reciept import print_receipt


def display_welcome_message():
    """Displays the welcome message."""

    print("\n" + "*" * 40)
    print(f"{'WELCOME TO FAST FOOD EXPRESS':^40}")
    print("*" * 40)


def display_exit_message():
    """Displays the exit message."""

    print("\nThank you for visiting! Have a great day!")


def ask_to_order():
    """Asks the customer if they want to place an order."""

    while True:
        user_choice = input(
            "Would you like to place an order? (yes/no): "
        ).strip().lower()

        if user_choice in ["yes", "y"]:
            return True

        elif user_choice in ["no", "n"]:
            return False

        else:
            print(
                "Invalid response. "
                "Please enter 'yes' or 'no'."
            )


def run_ordering_system():
    """Runs the complete ordering system."""

    display_welcome_message()

    # Ask if customer wants to order
    if not ask_to_order():
        display_exit_message()
        return

    order_list = []

    # Ordering loop
    while True:

        display_menu()

        # Select item
        item_choice = get_item_choice()

        # Enter quantity
        quantity = get_quantity(item_choice)

        # Add item to order
        add_item_to_order(
            order_list,
            item_choice,
            quantity
        )

        # Ask for another item
        if not ask_for_another_item():
            break

    # Print receipt
    if order_list:
        print_receipt(order_list)


# Start the program
if __name__ == "__main__":
    run_ordering_system()
