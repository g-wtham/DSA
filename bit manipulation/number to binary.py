def number2binary(num):
    res = ""
    while num > 0:
        if num%2 == 1:
            res += '1'
        else:
            res += '0'
            
        num = num // 2
     
    return res[::-1]
    
print(number2binary(5))
        