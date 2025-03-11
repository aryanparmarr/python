def move_zeros_to_end(arr):
    non_zero_elements = []
    
    for num in arr:
        if num != 0:
            non_zero_elements.append(num)
    
    zero_count = len(arr) - len(non_zero_elements)
    
    # Updating the array in place
    arr[:] = non_zero_elements + [0] * zero_count
    return arr

arr = [0, 1, 0, 3, 12]
modified_arr = move_zeros_to_end(arr)
print(modified_arr) 