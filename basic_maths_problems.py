import math

def print_all_divisors(n):
    sorted = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if (n%i == 0):
            sorted.append(i)
            if ((n//i) != i):
                sorted.append(n//i)
    sorted.sort()
    for j in sorted:
        print(j)
    
print_all_divisors(10)

def prime_numbers(n): 
    count_prime = 0  
    for i in range(1, int(math.sqrt(n) + 1)):
        if (n%i == 0):
            count_prime += 1
            if ((n/i) != i):
                count_prime += 1
    
    '''
    The condition if ((n / i) != i) ensures that for divisors i, the "mirror" divisor n / i is only counted if it is distinct from i. 
    This is especially useful for avoiding double-counting in the case of perfect squares.
    '''        
                
    if count_prime == 2:
        print("Prime")
    else:
        print("Not prime")

prime_numbers(789)