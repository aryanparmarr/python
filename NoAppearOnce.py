def findSingleElement(arr):
    result = 0
    for num in arr:
        result ^= num  # thia is the XOR function that terminates the pair
    return result
arr = [1, 1, 2, 2, 3, 4, 4, 5, 5]
result = findSingleElement(arr)
print(result)  