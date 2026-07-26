"""
Dish order explanation:
This program organizes dish IDs based on how often they appear.
Dishes with higher frequency are placed first, and if two dishes have the same frequency,
the lower dish ID appears first.

This is a useful pattern for ranking items by frequency and then by value.
"""


def DishPrepareOrder(order_list):
    """
    Sort dish IDs by frequency (descending) and then by dish ID (ascending).
    
    Args:
        order_list: A list of dish IDs (integers)
        
    Returns:
        A list of unique dish IDs sorted by:
        1. Frequency (most frequent first)
        2. If frequencies are equal, by dish ID (smaller ID first)
    """
    # Count how many times each dish ID appears
    counts = {}
    for dish_id in order_list:
        counts[dish_id] = counts.get(dish_id, 0) + 1

    # Get the unique dish IDs
    unique_dishes = list(counts.keys())

    # Sort by frequency descending, then by dish ID ascending
    # The key is a tuple: (-count, dish_id)
    # -count: negative so higher counts come first (descending order)
    # dish_id: positive so smaller IDs come first (ascending order)
    unique_dishes.sort(key=lambda x: (-counts[x], x))

    return unique_dishes
