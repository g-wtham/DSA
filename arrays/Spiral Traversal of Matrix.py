matrix = [[ 1,  2,  3,  4 ], 
          [ 5,  6,  7,  8 ], 
          [ 9,  10, 11, 12 ], 
          [ 13, 14, 15, 16 ]]

row = len(matrix) # Top to bottom see, its row
col = len(matrix[0]) # First list element items

top = left = 0
bottom = row-1
right = col-1

spiral = []

while (left <= right) and (top <= bottom):     # If left crosses right, or top crosses bottom, then we have covered the entire matrix and should stop.
    # l to r

    for i in range(left, right+1):
        spiral.append(matrix[top][i])
        
    top += 1   # So it moves 1 row down, as the last element in l to r is already added, we shouldn't add it again.     

    # top-right to bottom
    for j in range(top, bottom+1):
        spiral.append(matrix[j][right])
        
    right -= 1

    # If its a single-row matrix, when top +=1, if u move one row down, there is actually no rows,
    # if we continue moving `down -> left`, we will end up adding duplicate values. This condition prevents it.
    
    if (top <= bottom):            
        for k in range(right, left-1, -1):
            spiral.append(matrix[bottom][k])
        
        bottom -= 1

    if (left <= right):
        for l in range(bottom, top-1, -1):
            spiral.append(matrix[l][left])

        left += 1

print(spiral)