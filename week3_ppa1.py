"""
Dish order explanation:
This program organizes dish IDs based on how often they appear.
Dishes with higher frequency are placed first, and if two dishes have the same frequency,
the lower dish ID appears first.

This is a useful pattern for ranking items by frequency and then by value.
"""


def DishPrepareOrder(order_list):
    # Count how many times each dish ID appears.
    counts = {}
    for dish_id in order_list:
        counts[dish_id] = counts.get(dish_id, 0) + 1

    # Get the unique dish IDs.
    unique_dishes = list(counts.keys())

    # Sort by frequency descending, then by dish ID ascending.
    unique_dishes.sort(key=lambda x: (-counts[x], x))

    return unique_dishes
