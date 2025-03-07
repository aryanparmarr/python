def remove_duplicates(arr):
    
    
    n = len(arr)
    j = 0  
    
    for i in range(1, n):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]  # we can do this if the array given is sorted bcs every next value will be a duplicate or a unique value
    
    return j + 1