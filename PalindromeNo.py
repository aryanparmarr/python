n=int(input())  
def is_palindrome(n):
   
    str_n = str(n)
    
    
    return str_n == str_n[::-1]



if is_palindrome(n):
    print("true")
else:
    print("false")