def nStarDiamond(n: int) -> None:
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*(2*i-1))
    
    for j in range(1,n+1):
        print(" "*(j-1) +"*"*( 2 * (n - j + 1) - 1))   
    pass