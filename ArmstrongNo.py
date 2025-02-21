def checkArmstrong(n):
    digits = str(n)
    
   
    num_digits = len(digits)
    
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    
    print(sum_of_powers == n)
checkArmstrong(345)