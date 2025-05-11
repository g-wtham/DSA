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
    