from math import *
from collections import *
from sys import *
from os import *
def is_prime(n):
    if n <= 1:
        print("NO") 
        
    if n == 2:
        print("YES") 
        
    if n % 2 == 0:
        print("NO")  
        
   
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
             print("NO") 
             
    else:
        print("YES")
is_prime(5)