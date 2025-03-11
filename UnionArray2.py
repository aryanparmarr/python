# This is done using predefined functions
def union_of_arrays(a, b):
    # Convert both arrays to sets and find the union
    union_set = set(a) | set(b)
    
    # Convert the set to a sorted list
    result = sorted(union_set)
    
    return result
arr = [2,4,5,5,5,6,7,8,9]
b= set(arr)
print(b)