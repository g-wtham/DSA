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