def DishPrepareOrder(order_list):
    # Count frequency of each dish ID
    counts = {}
    for dish_id in order_list:
        counts[dish_id] = counts.get(dish_id, 0) + 1
    
    # Get unique dish IDs
    unique_dishes = list(counts.keys())
    
    # Sort: 
    # -x[1] sorts by frequency descending
    # x[0] sorts by dish ID ascending
    unique_dishes.sort(key=lambda x: (-counts[x], x))
    
    return unique_dishes
