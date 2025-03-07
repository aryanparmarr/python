def quick_sort(arr):  #time complexity is better for large dataset and the space complexity is also better then that of the merge sort because of the recursion stack
    if len(arr) <= 1:
        return arr  # Base case: if the array has 1 or fewer elements, it is already sorted
    
    # Step 1: Choose the pivot (choosing the last element here)
    pivot = arr[-1]
    
    # Step 2: Partition the array into two halves
    left = [x for x in arr[:-1] if x <= pivot]   # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]   # Elements greater than pivot
    
    # Step 3: Recursively apply quick_sort to the sub-arrays and combine them with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)