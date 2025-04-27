def f(n, sum):
    if n<1:
        print(sum)
        return 
    
    f(n-1, sum+n)

n = 5
f(5, 0)

def f(i, n):
    if n==0:
        print(i)
        return
    
    f(i+n, n-1)
    
n = 5
f(0, 5)

def f(i, n):
    if i > n:
        return 1
    return i + f(i+1, n)

n = 5
f(0, 5)

# If you are starting from 0 means, you are adding 0 at end when the call stack unwinds, which adds nothing and so no change
# If you start from 5 and put 0 (returned) for condition as i > n, it will work as it will return 0.
# If you start from 5 and put 1 (returned) for condition as i > n, it will like add one extra value.
# Eg: 6 > 5 => return 0 ----- 5 + 0 (crct) ; 6 > 5 => return 1 ----- 5 + 1 (wrong) [5+1, 4+6, 3+10, 2+13, 1+15 ==> 16]


def factorial(n):
    if n==1:
        return 1
    
    return n * factorial(n-1) 
    
print(factorial(10))

arr = [1,2,3,4,5]
i=0
j=len(arr)-1

while i<j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i+=1
    j-=1
    
print(arr)

def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
arr = [1,2,3,4,5]

def f(i, j):
    if i>j:
        return
    swap(i, j)
    f(i+1, j-1)

f(0, 4)    
print(arr)

arr = ['M','A', 'M']
arr2 = ['M','A', 'M']

def swap_pal(i, j):
    temp = arr[i]
    arr[j] = arr[i]
    arr[i] = temp

def palindrome(i, j):
    if j < i:
        return
    swap(i, j)
    palindrome(i+1, j-1)
    
palindrome(0, 2)
if arr == arr2:
    print("Palindrome")