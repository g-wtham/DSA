def maxDepth(s):
    count = 0
    maxC = 0
    for char in s:
        if char == '(':
            count += 1
            if count > maxC:
                maxC = count
        if char == ')':
            count -= 1

    return maxC
      
s = '(1+(2*3)+((8)/4))+1'          
print(maxDepth(s))
        