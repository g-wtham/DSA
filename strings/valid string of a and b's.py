'''
Problem: Valid String of A’s and B’s
You are given a string consisting of only 'A' and 'B'. The string is valid if:

Every 'A' must be followed by at least one 'B'.
The order should be any number of A’s, followed by at least the same number of B’s (e.g., "AABBB" is valid, but "AAABB" is not).
'''

str = 'ABABA'

def valid_stringAandB(str):
    count_a = 0
    count_b = 0
    flag = False
    for char in str:
        if char == 'A':
            if flag:
                return False
            count_a += 1
            
        elif char == 'B':
            count_b += 1
            flag = True
    
    if count_b >= count_a:
        return True
    else:
        return False

print(valid_stringAandB(str))
        
    
    
    