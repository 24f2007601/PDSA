"""
Minimum Platforms explanation:
This program calculates the minimum number of platforms needed at a railway station
so that all trains can be accommodated without any conflicts.

The key insight:
- When a train arrives, we need one more platform
- When a train departs, we free up one platform
- The maximum number of platforms needed at any time is our answer

This is similar to a meeting rooms problem where:
- Arrival = meeting start
- Departure = meeting end

We use a greedy approach:
1. Sort all arrivals and departures separately
2. Process events in chronological order
3. Count platforms needed at each point
4. Track the maximum count
"""


def minimum_platform(train_schedule):
    """
    Calculate the minimum number of platforms needed for all trains.
    
    Args:
        train_schedule: A list of tuples (train_no, arrival_time, departure_time)
                       where times are in 'HH:MM' format
                       
    Returns:
        The minimum number of platforms required
    """
    # Convert 'HH:MM' string to total minutes from midnight
    # This makes it easy to compare times and calculate durations
    def time_to_minutes(t_str):
        h, m = map(int, t_str.split(':'))
        return h * 60 + m

    # Separate arrival and departure times into two lists
    arrivals = []
    departures = []

    # Extract times and convert them to integer minutes
    for train_no, arr_time, dep_time in train_schedule:
        arrivals.append(time_to_minutes(arr_time))
        departures.append(time_to_minutes(dep_time))

    # Sort arrival and departure times independently
    # This allows us to process events in chronological order
    arrivals.sort()
    departures.sort()

    # Use two pointers to traverse the sorted lists
    i = 0  # Pointer for arrivals
    j = 0  # Pointer for departures
    platforms_needed = 0  # Current number of platforms in use
    max_platforms = 0  # Maximum platforms needed at any time

    # Process all arrival and departure events chronologically
    # Compare the next arrival with the next departure
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            # A train arrives (or arrives at the same time as another departs)
            # We need an additional platform
            platforms_needed += 1
            i += 1  # Move to the next arrival
            
            # Update the maximum platforms needed so far
            if platforms_needed > max_platforms:
                max_platforms = platforms_needed
        else:
            # A train departs, freeing up a platform
            platforms_needed -= 1
            j += 1  # Move to the next departure

    # Return the maximum number of platforms needed at any time
    # This ensures all trains can be accommodated
    return max_platforms


# Example usage with test data
# Each tuple is (train_no, arrival_time, departure_time)
print(minimum_platform([([(1,'09:00','09:10'),(2,'09:10','10:00'),(3,'10:50','11:20'),
                        (4,'11:25','11:30'),(5,'11:40','12:10'),(6,'12:15','13:00'),
                        (7,'13:06','13:10'),(8,'13:15','14:00'),(9,'14:05','15:00'),
                        (10,'18:00','20:00')])]))
