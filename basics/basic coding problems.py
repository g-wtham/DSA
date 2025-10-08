
# %%
def prime_factors(num):

    while num % 2 == 0:
        print(2)
        num = num//2

    i = 3
    while i < num:
        while num % i == 0:
            print(i)
            num = num//i
        i += 2

    if num > 1:
        print(num)

prime_factors(10)

# %%
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

n = 145

def strong_number(n):
    result = 0
    while n > 1:
        last_digit = n % 10
        result += factorial(last_digit)

        n = n//10

    return result == n

print(strong_number(n))

# %%

