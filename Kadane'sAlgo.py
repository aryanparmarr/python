"""You are given an array 'arr' of length 'n', consisting of integers.



A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.



Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays."""

def max_subarray_sum(arr):
    
    current_sum = 0
    max_sum = 0  
    
    for num in arr:
        
        current_sum = max(current_sum + num, num) # Kadane's algo
        
        
        max_sum = max(max_sum, current_sum)  # Kadane's algo
    
    return max_sum
