
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