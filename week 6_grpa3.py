def min_max(arr):
    n = len(arr)
    
    def max_heapify(i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check if left child exists and is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left
            
        # Check if right child exists and is larger than the largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right
            
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # Recursively heapify the affected sub-tree
            max_heapify(largest)

    # Build a max heap from the bottom-up (start from the last internal node)
    for i in range((n // 2) - 1, -1, -1):
        max_heapify(i)
