def linear_search(arr, k):
    for element in arr:
        if element == k:
            return True 
            
    return False 
arrr = [1,2,4,5,6,7,8,9,0]
a=linear_search(arrr,4)
print(a)
