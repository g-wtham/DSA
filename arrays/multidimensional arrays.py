def addMatrix(a, b):
    rows = len(a)
    col = len(a[0])
    
    result = []
    for _ in range(rows):
        result.append([0] * col) 
        
    for i in range(rows):
        for j in range(col):
            result[i][j] = a[i][j] + b[i][j]
        
    return result
    
A = [[1, 2, 3],  
     [4, 5, 6],  
     [7, 8, 9]]  

B = [[9, 8, 7],  
     [6, 5, 4],  
     [3, 2, 1]]   
    
print(addMatrix(A, B))