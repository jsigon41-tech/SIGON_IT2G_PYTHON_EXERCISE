# reciept.py

from discount import calculate_discount


def calculate_order_totals(order_list):
    """Calculates subtotal, discount, and grand total."""

    subtotal = 0.0

    for item in order_list:
        subtotal += item["item_total"]

    discount = calculate_discount(subtotal)

    grand_total = subtotal - discount

    return subtotal, discount, grand_total


def print_receipt(order_list):
    """Prints the customer's receipt."""

    subtotal, discount, grand_total = calculate_order_totals(order_list)

    print("\n" + "=" * 45)
    print(f"{'FAST FOOD EXPRESS RECEIPT':^45}")
    print(f"{'Official Order Summary':^45}")
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
