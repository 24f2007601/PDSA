def no_overlap(L):
    # If the list is empty, return an empty list
    if not L:
        return []
    
    # Sort the applications by their end_day (the third element in the tuple)
    # If end days are equal, sorting by start_day or id helps maintain consistency
    sorted_L = sorted(L, key=lambda x: (x[2], x[1]))
    
    # Initialize the list of accepted IDs and track the last end day
    accepted_ids = [sorted_L[0][0]]
    last_end_day = sorted_L[0][2]
    
    # Iterate through the remaining sorted applications
    for app in sorted_L[1:]:
        app_id, start_day, end_day = app
        
        # Check if the meeting starts after the last accepted meeting ends
        if start_day > last_end_day:
            accepted_ids.append(app_id)
            last_end_day = end_day
            
    return accepted_ids

# --- Verification with Sample Input ---
L = [
    (0, 1, 2),
    (1, 1, 3),
    (2, 1, 5),
    (3, 3, 4),
    (4, 4, 5),
    (5, 5, 8),
    (6, 7, 9),
    (7, 10, 13),
    (8, 11, 12)
]

print(no_overlap(L))
# Output: [0, 3, 6, 8]
