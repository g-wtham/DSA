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

def gcd(n1, n2):
    gcd = 1
    for i in range(min(n1, n2), 1, -1): # Running till min(n1, n2) is enough, as GCD of 2 numbers cant exceed the minimum one, as it has to be the common highest factor.
        if (n1%i == 0 and n2%i == 0):   # Remember, 'i' is the NUMBER which divides the GIVEN number iteratively (current iteration, i == current divisor of GIVEN NO.)
            gcd = i
            break
    return gcd

print(gcd(32, 97))

def rev_number(n):
    rev = 0
    while (n != 0):
        lastDigit = n%10
        rev = (rev * 10) + lastDigit
        n = n // 10
    return rev

print(rev_number(225))

def palindrome_check(n):
    dup = n
    rev = 0
    while (n != 0):
        lastDigit = n%10
        rev = (rev * 10) + lastDigit
        n = n // 10
    if (rev == dup):
        print("Palindrome")
    else:
        print("Not a palindrome")
        
palindrome_check(252)