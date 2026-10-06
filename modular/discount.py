# discount.py

DISCOUNT_RATE = 0.10
DISCOUNT_MINIMUM = 200.00


def calculate_discount(subtotal):
    """Calculates the discount based on the subtotal."""

    if subtotal >= DISCOUNT_MINIMUM:
        return subtotal * DISCOUNT_RATE

    return 0.0

