
# %% 
# Fibonacci Series upto nth term
# 0, 1, 1, 2, 3, 5

n = 10
def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

for i in range(n):
    print(fib(i))

# %%
# prime factorization 

from math import sqrt

def prime_factors(num):
    if num <= 1:
        return num

    # does for factors of 2     
    while num % 2 == 0:
        print(2)
        num = num // 2

    i = 3
    while i <= int(sqrt(num)+1):
        while num % i == 0:
            print(i)
            num = num//i
        i += 2

    if num > 1:
        print(num)

prime_factors(10)

# %%

# Strong Number 

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

n = 145

def strong_number(n):
    num = n
    result = 0
    while n > 0:
        last_digit = n % 10
        result += factorial(last_digit)
        n = n//10

    return result == num

print(strong_number(n))

# %%

# perfect number

def factors(num):
    list1 = []
    i = 1
    while i < num:
        if num % i == 0:
            list1.append(i)
        i += 1
    return list1

def perfect_number(num):
    if sum(factors(num)) == num:
        print("Perfect Number")
    else:
        print("Not a perfect number")

perfect_number(28)
# %%

# Perfect Square

n = 36
sr = int(n**0.5)
print((sr * sr) == n)

# %%

# Friendly Pair

def factors(num):
    list1 = []
    i = 1
    while i < num:
        if num % i == 0:
            list1.append(i)
        i += 1
    return list1

a, b = 6, 28

def friendly_pair(a, b):
    sum1, sum2 = sum(factors(a)), sum(factors(b))
    if sum1 / a == sum2 / b:
        return "Friendly Pair"
    else:
        return "Not friendly pair"
    
friendly_pair(a, b)

# %%
#  Abundant Number

def factors(num):
    list1 = []
    i = 1
    while i < num:
        if num % i == 0:
            list1.append(i)
        i += 1
    return list1

def abundant_numbers(num):
    if (sum(factors(num)) > num):
        return "Abundant Number"
    else:
        return "Not Abundant Number"
    
abundant_numbers(12)

# %%

# Expressing number interms of 2 prime numbers
from math import sqrt

def is_prime(num):
    if num <= 1:
        return False 
    
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
        
    return True

def sum_prime(num):
    for i in range(2, num+1):
        if is_prime(i):
            target = num - i
            if is_prime(target):
                if i + target == num:
                    print(i, target)
                    return True
                else:
                    return False          
sum_prime(15)

# %%





