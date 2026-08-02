def minimum_platform(train_schedule):
    # Convert 'HH:MM' string to total minutes from midnight
    def time_to_minutes(t_str):
        h, m = map(int, t_str.split(':'))
        return h * 60 + m

    arrivals = []
    departures = []

    # Extract times and convert them to integers
    for train_no, arr_time, dep_time in train_schedule:
        arrivals.append(time_to_minutes(arr_time))
        departures.append(time_to_minutes(dep_time))

    # Sort arrival and departure times independently
    arrivals.sort()
    departures.sort()

    i = 0
    j = 0
    platforms_needed = 0
    max_platforms = 0

    # Process all arrival and departure events chronologically
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
            if platforms_needed > max_platforms:
                max_platforms = platforms_needed
        else:
            platforms_needed -= 1
            j += 1

    # CRITICAL: This line must be aligned with the 'while' block
    return max_platforms
print(minimum_platform([([(1,'09:00','09:10'),(2,'09:10','10:00'),(3,'10:50','11:20'),(4,'11:25','11:30'),(5,'11:40','12:10'),(6,'12:15','13:00'),(7,'13:06','13:10'),(8,'13:15','14:00'),(9,'14:05','15:00'),(10,'18:00','20:00')])]))
