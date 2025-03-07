def find_second_largest_and_second_smallest(arr):
    # Initialize the smallest and largest elements with very large and very small values
    smallest = float('inf')
    largest = -float('inf')
    second_smallest = float('inf')
    second_largest = -float('inf')
    
    
    for num in arr:
        if num < smallest:
            second_smallest = smallest  
            smallest = num  
        elif num < second_smallest:
            second_smallest = num 
        
        if num > largest:
            second_largest = largest 
            largest = num  
        elif num > second_largest:
            second_largest = num 
    
   
    return [second_largest, second_smallest]