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
        
def binary2number(binary_num):      
    num = 0
    for i in range(len(binary_num)-1, -1, -1):
        num += int(binary_num[i]) * int((2**(len(binary_num)-1-i)))
           
    return num   
           
print(binary2number("1101"))