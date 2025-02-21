def nBinaryTriangle(n):
    for i in range(1, n + 1): 
        row = [] 
        
     
        for j in range(i,i+i):  
           
            row.append(str(j % 2))
        
        
        print(" ".join(row))
nBinaryTriangle(4)