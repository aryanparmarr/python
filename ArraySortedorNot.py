def is_sorted(arr):
    n = len(arr)
    
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return 0 
    
    return 1