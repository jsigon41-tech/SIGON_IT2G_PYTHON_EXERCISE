# food.py

MENU = {
    1: {"name": "Burger", "price": 50.00},
    2: {"name": "Fries", "price": 30.00},
    3: {"name": "Fried Chicken", "price": 80.00},
    4: {"name": "Spaghetti", "price": 60.00},
    5: {"name": "Soda", "price": 25.00}
}


def display_menu():
    """Displays the menu items."""
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
