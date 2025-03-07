def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted into the sorted portion
        j = i - 1  # The index of the last element in the sorted portion

        # Move elements of arr[0..i-1] that are greater than the key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key after shifting larger elements
        arr[j + 1] = key
        
    return arr