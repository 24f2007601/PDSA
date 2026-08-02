"""
Meeting Rooms / Activity Selection explanation:
This program finds the maximum number of non-overlapping activities (meetings) that can be scheduled.
This is a classic greedy algorithm problem.

The key insight (Greedy Choice):
- Always pick the activity that ends earliest
- This leaves maximum time for remaining activities
- If the next activity starts after the current one ends, we can include it

This is optimal because:
1. Activities that end earlier leave more room for others
2. Any optimal solution can be transformed into this greedy solution
3. We maximize the count by minimizing the time each activity occupies
"""


def no_overlap(L):
    """
    Find the maximum number of non-overlapping meetings.
    
    Each meeting is represented as a tuple: (id, start_day, end_day)
    We want to select the maximum number of meetings such that no two overlap.
    
    Greedy Strategy:
    1. Sort meetings by their end day (earliest finishing first)
    2. Select a meeting if it starts after the last selected meeting ends
    3. Repeat until all meetings are considered
    
    Args:
        L: A list of tuples (meeting_id, start_day, end_day)
        
    Returns:
        A list of meeting IDs that can be scheduled without overlap
    """
    # If the list is empty, return an empty list
    if not L:
        return []
    
    # Sort the applications by their end_day (the third element in the tuple)
    # If end days are equal, sorting by start_day helps maintain consistency
    # This is the key greedy step: earliest finishing meetings go first
    sorted_L = sorted(L, key=lambda x: (x[2], x[1]))
    
    # Initialize the list of accepted IDs and track the last end day
    # The first meeting is always accepted since nothing came before it
    accepted_ids = [sorted_L[0][0]]
    last_end_day = sorted_L[0][2]
    
    # Iterate through the remaining sorted meetings
    for app in sorted_L[1:]:
        app_id, start_day, end_day = app
        
        # Check if the meeting starts after the last accepted meeting ends
        # If yes, we can schedule this meeting without overlapping
        if start_day > last_end_day:
            accepted_ids.append(app_id)
            last_end_day = end_day  # Update the last end day
            
    return accepted_ids


# --- Verification with Sample Input ---
# Each tuple is (meeting_id, start_day, end_day)
L = [
    (0, 1, 2),   # Meeting 0: day 1 to 2
    (1, 1, 3),   # Meeting 1: day 1 to 3
    (2, 1, 5),   # Meeting 2: day 1 to 5
    (3, 3, 4),   # Meeting 3: day 3 to 4
    (4, 4, 5),   # Meeting 4: day 4 to 5
    (5, 5, 8),   # Meeting 5: day 5 to 8
    (6, 7, 9),   # Meeting 6: day 7 to 9
    (7, 10, 13), # Meeting 7: day 10 to 13
    (8, 11, 12)  # Meeting 8: day 11 to 12
]

print(no_overlap(L))
# Output: [0, 3, 6, 8]
