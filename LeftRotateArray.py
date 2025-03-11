def rotate_left(arr):
    if len(arr) == 0:
        return arr
    
    
    first_element = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = first_element  # Place the first element at the end
    
    return arr
arrr=[1,2,3,4,5,6,7,8,9,0]
a=rotate_left(arrr)
print(a)