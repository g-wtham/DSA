def addition_without(a, b):
    
    while b != 0:
        sum = a ^ b  # gives us the raw sum without carry
        carry = (a & b) << 1  # gives us the carry shifted to left by 1

        a = sum
        b = carry
        
    return sum

print(addition_without(2, 5))

def swap_num(a, b):
    print(f"Original: a={a}; b={b}")
    
    a = a ^ b
    b = a ^ b  # a ^ b ^ b = a; b = a; a ^ a ^ b
    a = a ^ b
    
    print(f"Swapped: a={a}; b={b}")
    
swap_num(3, 5)

# %%
def unique_num_using_xor(num):
    result = 0
    for number in num:
        result ^= number
        
    print(result)
    
    
nums = [2, 3, 5, 4, 5, 3, 4]
unique_num_using_xor(nums)

# %%
