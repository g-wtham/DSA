# a = input("Please type in the 1st word:")
# b = input("Please type in the 2nd word:")
# if a > b:
#     print(f"{a} comes alphabetically last.")
# if a == b:
#     print("You gave the same word twice.")

'''
Please write a program which asks the user for an integer number.
If the number is divisible by three, the program should print out Fizz. 
If the number is divisible by five, the program should print out Buzz.
If the number is divisible by both three and five, the program should print out FizzBuzz.
'''

# %%
a = int(input())
if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
elif a % 3 == 0:
    print("Fizz")
else:
    print("Buzz")

# %%
x = int(input())
if x % 4 == 0:
    if x%100 == 0 and x%400 == 0:
        print("Leap year")
    print("leap year")
else:
    print("Not a leap year")


    
# %%

x1 = input()
x2 = input()
x3 = input()

if x1 > x2 and x1 < x3 or x1 < x2 and x1 > x3:
    print(x1)
elif x2 > x1 and x2 < x3 or x2 < x1 and x2 > x3:
    print(x2)
else:
    print(x3)
# %%
x1 = input("Value:1")
x2 = input("2")
x3 = input("3")

if x1<x2 and x1<x3:
    if x2<x3:
        middle = x2
    else:
        middle = x3
        
elif x2<x1 and x2<x3:
    if x1<x3:
        middle = x1
    else:
        middle = x3
        
else:
    if x2<x1:
        middle = x2
    else:
        middle = x1
        
print(middle)
# %%

a = int(input("Value of gift"))
if a < 5000:
    print("No tax!")
    
elif a >= 5000 and a < 25000:
    tax = (100 + (a-5000) * 0.08)
    
elif a >= 25000 and a < 55000:
    tax = (1700 + (a-25000) * 0.10)
    
elif a >= 55000 and a < 200000:
    tax = (4700 + (a-55000) * 0.12)
    
elif a >= 200000 and a < 1000000:
    tax = (22100 + (a-200000) * 0.15)

else:
    tax = (142100 + (a-1000000) * 0.17)
    
print(tax)
    
# %%
while True:
    print("Hi")
    val = input("Shall we continue?")
    if val == 'no':
        print("okay then")
        break
# %%
from math import sqrt

while True:
    a = int(input("Please type in a number:"))
    if a < 0:
        print("Invalid Number")
    elif a > 0:
        print(sqrt(a))
    else:
        break
# %%

number = 5
print("Countdown!")
while True:
    print(number)
    number = number - 1
    if number == 0:
        break

print("Now!")
# %%
while True:
    a = input("Password:")
    b = input("Repeat Password:")
    if a!=b:
        print("they do not match!")
    if a==b:
        break
print("User account created")


# %%
attempts = 0
while True:
    a = int(input("PIN:"))
    if a == 4321:
        if attempts == 0:
            print("Correct! It only took you one single attempt!")
            break
        else:
            print(f"Correct! It took you {attempts} attempts")
            break
    attempts += 1
    print("Wrong")
    
# %%
while True:
    a = int(input("Year: "))
    if a == 2006:
        print("Thanks")
        break
    remainder = a % 4
    needed = 4 - remainder
    print(f"The next leap year after {a} is {a + needed}")


# %%
story = ""
last_word = ""
while True:
    a = input("Please type in a word:").strip()
    if a == last_word:
        print(story)
        break
    if a == "end":
        print(story)
        break
    last_word = a
    story += a + " "
    
    
    
# %%
attempts = 0
sum_value = 0
positive = 0
negative = 0
while True:
    a = int(input("Number:"))
    
    if a != 0:
        attempts += 1
        sum_value += a
        
    if a>0:
        positive += 1
    elif a<0:
        negative += 1  
    
    if a == 0:
        print("Numbers typed in", attempts)
        print('Sum: ', sum_value)
        print('The mean of the numbers is', sum_value/attempts)
        print("Positive: ", positive)
        print("Negative: ", negative)
        break
    
# %%
i = 2
while i < 30:
    print(i)
    i+=2
# %%
a = int(input("Number:"))
i = 1
while i<a:
    print(i)
    i+=1
# %%
a = int(input("Number:"))
j=0
while True:
    i = 2**j
    if i>a:
        break
    print(i)
    j += 1
# %%
a = int(input("Number:"))
j=1
while j<a:
    print(j) 
    j *= 2   
# %%
a = int(input("Number:"))
b = int(input("Base: "))
j=1
v=1
while v<=a:
    print(v)
    v = b**j
    j+=1
# %%
limit = int(input("Limit: "))
sum_value = 0
while sum_value <= limit:
    sum_value += 1
    print("sum:",sum_value)
print(sum_value)


# %%
limit = int(input("Limit: "))

output = 1
calculation = ""
while output <= limit:
    if calculation:
        calculation += "+"
    calculation += f"{output}"
    output += 1
    
print(f"The consecutive sum: {calculation}= {output}")
    
# %%
u = int(input())
b = int(input())
power = 0
output = 0
while output <= u:
    output = b**power
    if output <= u:
        print(output)
    power += 1
# %%
n = 5
stars = "*"
while n > 0:
    print(" " * n + stars)
    stars += '**'
    n -= 1
# %%
a = input()
b = int(input())
print(a*b, end="")
# %%
w = int(input())
h = int(input())

for i in range(h):
    for j in range(w):
        print("#", end="")
    print() 
# %%
l = input()
input_length = len(l)
if input_length <= 20:
    print((20-input_length) * "*" + l)
else:
    print(l)

# %%
word = input()
word_len = len(word)
print("*" * 30)
spaces = (28 - word_len)//2
if word_len %2 == 0:
    print("*" + " " * spaces + word + " " * spaces + "*")
else:
    print("*" + " " * spaces + word + " " * (spaces+1) + "*")

print("*" * 30)

# %%
word = input()
so_far = ""
for i in range(len(word)-1, -1, -1):
    so_far = word[i] + so_far
    print(so_far)
# %%
word = input()
if 'a' in word:
    print("a found")
else:
    print("a not found")
#%%
word = input()
char = input()
first_char_index = word.find(char)
if first_char_index + 3 <= len(word) and char in word:
    print(word[first_char_index:first_char_index+3])
else:
    print("Nothing!")
#%%

# SOLVED IN JUST 2-3 TRY WITHOUT GOOGLING
word = input()
char = input()
j = 0
while j<len(word):
    i = word.find(char)
    if i + 3 <= len(word):
        print(word[i:i+3])
    j+=1
    word = word[j:]
    
#%%
string = input()
substring = input()
if substring in string:
    i = string.find(substring)
    old_index = i
    string = string[i+1:]
    if substring in string:
        i = string.find(substring)
        i = i+1   # Since 2nd slicing starts from 0 and not 1, need to compensate for it.
        print("The second occurrence of the substring is at index", old_index + i)
    
#%%
value = int(input())
i = 1
while i <= value:
    j = 1
    while j<=value:
        print(i ,'x', j, '=', i*j)
        j+=1 
    i+=1
#%%
string = input()
first_char = True
for char in string:
    if first_char:
        print(char)
        first_char = False
    if char == ' ':
        first_char = True
        
        
        
#%%
string = input()
first_char = False
for char in string:
    if not first_char:
        print(char)
        first_char = True
    if char == ' ':
        first_char = False
# %%
number = int(input())
i = number-1
while i > 0:
    number = number * i
    i -= 1
print(number)

# %%
'''
1st odd = save dont print
2nd even = print
print 1st odd
'''

number = int(input("Please type in a number: "))
for i in range(1, number+1):
    if number % 2 != 0:
        odd = number
    else:
        even = number




# %%
