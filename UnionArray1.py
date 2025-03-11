# This code is done without using predefined functions
def union_of_arrays(a, b):
    # Initialize pointers for both arrays
    i, j = 0, 0
    result = []
    
    # Traverse both arrays
    while i < len(a) and j < len(b):
        # If both elements are the same, add it to the result and move both pointers
        if a[i] == b[j]:
            if not result or result[-1] != a[i]:  # Avoid duplicates
                result.append(a[i])
            i += 1
            j += 1
        # If element in a is smaller, add it to result and move pointer in a
        elif a[i] < b[j]:
            if not result or result[-1] != a[i]:  # Avoid duplicates
                result.append(a[i])
            i += 1
        # If element in b is smaller, add it to result and move pointer in b
        else:
            if not result or result[-1] != b[j]:  # Avoid duplicates
                result.append(b[j])
            j += 1
    
    # If there are remaining elements in a, add them
    while i < len(a):
        if not result or result[-1] != a[i]:
            result.append(a[i])
        i += 1
    
    # If there are remaining elements in b, add them
    while j < len(b):
        if not result or result[-1] != b[j]:
            result.append(b[j])
        j += 1
    
    return result

a = [1, 2, 4, 5, 6]
b = [2, 3, 5, 7]

result = union_of_arrays(a, b)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7]

