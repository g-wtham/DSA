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
n = 3
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
i = 1
while i <= number:
    if i + 1 <= number:
        print(i+1)
    print(i)
    i += 2

# %%
number = int(input("Please type in a number: "))
'''
4 3 2 1
'''

i = 1
j = number
while i <= j:
    print(i)
    if i != j:
        print(j)
    i += 1
    j -= 1

# %%
number = int(input("Please type in a number: "))
total = 0
for i in range(1, number+1):
    if i % 2 == 0:
        total -= i
    else:
        total += i
   
print(total)     
# %%
number = int(input("Please type in a number: "))
j = 0
for i in range(1, number+1):
    if i % 3 == 0:
        for num in range(i, j, -1):
            print(num)
        j = i
        
# j = 6; number = given
for k in range(number, j, -1):
    print(k)
    
    
# %%
n = int(input())
start = 1
for _ in range(n):
    for _ in range(n):
        print(start, end="")
        start = 1 - start
    print()

# %%
def squared(string, number):
    for i in range(number):
        final_string = ""
        for j in range(number):
            final_string += string[(i+j) % len(string)]
        print(final_string)    
      
squared('ab', 3)  
# %%
def line(integer, string):
    if string == "":
        return '*' * integer
    else:
        return string[0] * integer
        
print(line(7, ""))

def box_of_hashes(num):
    for _ in range(num):
        print(line(10, '#'))
    
box_of_hashes(5)



def square(integer, string):
    for _ in range(integer):
        print(line(integer, string))
            
print(square(5, "*"))

def triangle(number):
    i = 1
    while i <= number:
        print(line(i, '#'))
        i += 1
        
triangle(3) 


def shape(width, char, height, filler):
    i = 1
    while i <= width:
        print(line(i, char))
        i += 1
    j = 0
    while j < height:
        print(line(width, filler))
        j += 1
        
shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")
# %%
def spruce(num):
    nam = 1
    i = 1
    n = num-1
    while i <= num:
        print(" " * n + '*' * nam)
        n -= 1
        i += 1
        nam += 2
    print(" " * (num-1) + '*')

spruce(5)
# %%
def first_word(sentence):
    first = ""
    for i in range(len(sentence)):
        if sentence[i] != " ":
            first += sentence[i]
        if sentence[i] == ' ':
            break
    print(first)
    
first_word("it was a dark and stormy python")

# %%
def second_word(sentence):
    second = ""
    count = 0
    for i in range(len(sentence)):
        if sentence[i] == " ":
            count += 1
        if count == 1:
            second += sentence[i+1]
    print(second)

second_word("it was a dark and stormy python")
# %%
def third_word(sentence):
    third = ""
    count = -1
    for i in range(len(sentence)):
        if sentence[i] == " ":
            count = i
    third += sentence[count+1:len(sentence)]
    
    return third

print(third_word("it was"))

# %%
listI = []
for i in range(3):
    items = int(input(f"Item {i+1}: "))
    listI.append(items)
print(listI)
# %%
my_list = []
value = 0
while True:
    print(f"The list is now {my_list}")
    option = input("a(d)d, (r)emove or e(x)it: ")
    if option == 'd':
        if len(my_list) == 0:
            value = 0
        value += 1
        my_list.append(value)
    if option == 'r':
        if len(my_list) == 0:
            print("Empty List")
            continue
        my_list.pop(-1)
    if option == 'x':
        print("Bye!")
        break
# %%
my_list = []
while True:
    value = input("Word: ")
    if value in my_list:
        print(f"You typed in {len(my_list)} different words")
        print(*my_list)   # unpacks list
        break
    if value not in my_list:
        my_list.append(value)
        
#%%

value = input("Word: ")
for char in value:
    print(char)
    print('*')

#%%
value = int(input("Word: "))
for i in range(-value, value+1):
    if i == 0:
        continue
    print(i)
# %%
my_list = [3, 2, 2, 1, 3, 3, 1]
def distinct_numbers(my_list):
    unique = []
    for num in my_list:
        if num not in unique:
            unique.append(num)
    
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if unique[j] < unique[i]:
                unique[j], unique[i] = unique[i], unique[j]
        
    return unique

distinct_numbers(my_list)
# %%
def length_of_longest(my_list):
    initial = my_list[0]
    for item in my_list:
        if len(item) > len(initial):
            initial = item
    return len(initial)

my_list = ["first", "second", "fourth", "eleventh"]

length_of_longest(my_list)
# %%
def all_the_longest(my_list):
    length = 0
    initial = my_list[0]
    
    for item in my_list:
        if len(item) > len(initial):
            initial = item
            length = len(item)
    
    long = []
    for item in my_list:
        if len(item) == length:
            long.append(item)
 
    return long

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

all_the_longest(my_list)

# %%
my_list = [1.234, 0.3333, 0.11111, 3.446]
def formatted(my_list):
    list1 = []
    for item in my_list:
        word = f"{item:.2f}"
        list1.append(str(word)) 
        
    return list1

formatted(my_list)

    
# %%
def most_common_character(string):
    char_dict = {}
    for ch in string:
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1
    
    max_count = 0
    max_ele = ""
    for char in string:
        if char_dict[char] > max_count:
            max_ele = char
            max_count = char_dict[char]
    
    return max_ele, max_count

most_common_character("exemplaryelementary")
# %%
my_string = "this is an example"
vowels = "aeiou"
string = ""
for ch in my_string:
    if ch not in vowels:
        string += ch
        
print(string)
# %%
my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
pruned_list = []
for item in my_list:
    if not item.isupper():
        pruned_list.append(item)
print(pruned_list)
# %%
string = "eabccdbe"
duplicate_detect = True
indices = []
for i in range(len(string)):
    for j in range(i+1, len(string)):
        if string[i] == string[j]:
            duplicate_detect = False
            indices.append(j)

if duplicate_detect:
    print("No duplicate")
else:
    print("Dup found!")
    for i in indices:
        print(f"{string[i]} = {i}", end=" ")
# %%
my_list = [1,2,3,4,5,6,7,8]
print(my_list[len(my_list)-2:0:-1])
# %%
first_string = "abbcdddbe"
max = 0
list1 = []
for char in first_string:
    current_count = first_string.count(char)
    if current_count > max:
        max = current_count
        character = char
        list1.append(max)

print(character)
print(list1)
# %%
my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
list2 = []
for item in my_list:
    if not item.isupper():
        list2.append(item)
print(list2)

# In-place modification 
for i in range(len(my_list)-1, -1, -1):
    if my_list[i].isupper():
        my_list.pop(i)
print(my_list)
# %%
def longest_series_of_neighbours(arr):
    count = 1
    max_count = 0
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) == 1:
            count += 1
            if count > max_count:
                max_count = count
                temp_start = (i+1)-max_count
                arr1 = arr[temp_start: temp_start+max_count]
        else:
            count = 1
            
    return max_count, arr1

my_list = [1, 2, 5, 4, 3, 4]
print(longest_series_of_neighbours(my_list))

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))
# %%
names = ["Marlyn", "David", "Ruth", "Paul"]
for i in range(len(names)):
    for j in range(1, len(names)-i):
        if names[j-1] > names[j]:
            names[j-1], names[j] = names[j], names[j-1]
            
print(names)
# %%
def distinct_numbers(arr):
    list1 = []
    for num in arr:
        if num in list1:
            return False
        list1.append(num)
    
    return True
    
distinct_numbers([1, 2, 2])
# %%
longest = 0
strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
for str in strings:
    if len(str) > longest:
        longest = len(str)
        string1 = str
print(string1)
# %%
def sum_of_row_column(m, col_no: int):
    col_sum = 0
    for row in m:
        col_sum += row[col_no]
        
    row_sum = 0
    row = m[col_no]
    
    for ele in row:
        row_sum += ele
        
    return col_sum, row_sum

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]
sum_of_row_column(m, 1)
        
# %%

# If just accessing all the elements just traversing the matrix with `for item in items` is enough. 
# If we want to access or modify it, by means of using a `for loop` with range() or a while loop so that the INDEX can be noted and used for modifying the elements.

# %%

m = [[1,2,3], [4,6], [7,8,9]]

for i in range(len(m)): # using the number of rows in the matrix
    for j in range(len(m[i])): # using the number of items on each row 
        m[i][j] += 1

print(m)

'''
range = 3 (0 1 2)
1st iteration :
i = 0
No iteration at all

2nd :
i = 1 
j = 0 => [0] (as 1 is exclusive)
[1, 0]

3rd :
i = 2
j = 0, 1
[2,0] [2,1]
'''
# %%
m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
argument = 1
count = 0
for item in m:
    for ele in item:
        if ele == argument:
            count += 1
print(count)
# %%
a = 10
print(id(a))
a += 12
print(id(a))
a = 10
print(id(a))

# %%
def double_items(numbers: list):
    new_list = []
    for item in numbers:
        new_list.append(item*2)
     
    return new_list
    
numbers = [2, 4, 5, 3, 11, -4]
numbers_doubled = double_items(numbers)
print("original:", numbers)
print("doubled:", numbers_doubled)
    
# %%
def remove_smallest(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
            
    numbers[:] = numbers[1:n]
    
numbers = [2, 4, 6, 1, 3, 5]
remove_smallest(numbers)
print(numbers)

# %%
def play_turn(gameboard, x, y, piece):
    if gameboard[y][x] == "":
        gameboard[y][x] = piece
        return True
    else:
        return False
    
game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
print(play_turn(game_board, 2, 0, "X"))
print(game_board)

# %%

# Transpose a matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
        
print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[j][i], end=" ")
    print()
# %%
def times_ten(start_index: int, end_index: int):
    dict1 = {}
    for i in range(start_index, end_index+1):
        dict1[i] = 10 * i
        i += 1
    return dict1
        
times_ten(3, 6)

# %%
def factorials(n: int):
    dict1 = {}
    i = n
    value = i-1
    while i > 0:
        value = value * i
        dict1[i] = value
        i += 1
    return dict1

k = factorials(5)
print(k[1])
print(k[3])
print(k[5])
# %%

word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

def categorize_by_initial(my_list):
    dict1 = {}
    for item in my_list:
        initial = item[0]
        
        if initial not in dict1:
            dict1[initial] = []
            
        dict1[initial].append(item)
    
    for key, values in dict1.items():
        print("Words beginning with ", key)
        values.sort()
        for value in values:        # since values is a list and we need to print one by one
            print(value)
   
categorize_by_initial(word_list)        
        
# %%
def histogram(string: str):
    dict1 = {}
    
    for ch in string:
        if ch in dict1:
            dict1[ch] += '*'
        
        else:
            dict1[ch] = '*'
        
    for key, value in dict1.items():
        print(key, value)
    
histogram("statistically") 
# %%
<<<<<<< HEAD
dict1 = {}
while True:
    option = int(input("command (1 search, 2 add, 3 quit): "))
    if option == 3:
        print("quitting...")
        break
    
    if option == 1:
        search_key = input("name: ")
        if dict1[search_key]:
            print(dict1[search_key])
        else:
            print("no number")
        
    if option == 2:
        key = input("name: ")
        value = input("number: ")
        dict1[key] = value
        print("ok")
# %%
dict1 = {}
while True:
    option = int(input("command (1 search, 2 add, 3 quit): "))
    if option == 3:
        print("quitting...")
        break
    
    if option == 1:
        search_key = input("name: ")
        if search_key in dict1:
            value_list = dict1[search_key]
            for item in value_list:
                print(item)
        else:
            print("no number")
        
    if option == 2:
        key = input("name: ")
        value = input("number: ")
       
        if not key in dict1:
            dict1[key] = []
        
        dict1[key].append(value)
# %%
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}

def invert(s: dict):
    copy_s = s.copy()
    s.clear()
    for key, value in copy_s.items():
        s[value] = key
        
    return s

print("Original: ", s)
print("Reveresed: ", invert(s))
    
# %%
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    dict1 = {}
    dict1["name"] = name
    dict1["director"] = director
    dict1["year"] = year
    dict1["runtime"] = runtime
    database.append(dict1)
    
database = []
add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
print(database)
    
=======

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Empty stack")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Empty Stack")

    def isEmpty(self):
        if not self.stack:
            return "Empty stack"
        else:
            return "Not empty"
        
    def traversal(self):
        print(self.stack)
        
stack = Stack()
stack.push(10)
stack.push(30)
stack.push(20)
stack.traversal()
print(stack.pop())
print(stack.peek())
stack.traversal()
print(stack.isEmpty())

# %%
# Problem: Given N strings, find the first longest string with odd length. 
# If none exists, output "Better luck next time".

string = input("String: ")
max = ""
flag = False
for word in string.split():
    if len(word) % 2 != 0:
        if len(word) > len(max):
            flag = True
            max = word
if flag:
    print(max)
else:
    print("Better luck next time")
  
  

# %%
# Problem: Given an array of stock prices, one transaction allowed.
# Buy and sell once to maximize profit.

stocks = [1, 9, 2, 11, 1, 9, 2]
min = float('inf')
max_profit = 0
for stock in stocks:
    if stock < min:
        min = stock
    profit = stock - min
    if profit > max_profit:
        max_profit = profit

print(max_profit)
# %%

# Method: 1
n = int(input())
sum_value = 0
for i in range(1, n+1):
    sum_value += i * i
print(sum_value)

# Method: 2
n = int(input())
sum_value = (n * (n+1) * (2*n + 1)) // 6
print(sum_value)

# %%
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
del1 = s.pop(5, "Not Found")
print(del1)

s_copy = s.copy()
s.clear()
for key, value in s_copy.items():
    s[value] = key  
print(s)
# %%
tup1 = {}
tup1[(1,2,3)] = "Gowtham"
print(tup1[(1,2,3)])
print(tup1)
# %%

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]
def oldest_person(people: list):
    min = float('inf')
    name = ""
    for item in people:
        if item[1] < min:
            min = item[1]
            name = item[0]
    return name       
oldest_person(people)    
# %%
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

def older_person(people: list, year: int):
    names = []
    for item in people:
        if item[1] < year:
            names.append(item[0])
    return names        
older_person(people, 1979)    
# %%
students = {}
def add_student(students: dict, name: str):
    students[name] = []
    
def print_student(students: dict, name: str):    
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}: ")
        courses = students[name]
        print(f" {len(courses)} completed courses:")
        total_grades = 0
        for course, grade in courses:
            print(f"  {course} {grade}")
            total_grades += grade
        print(f"average grade {total_grades / len(courses)}")
        if not courses:
            print("  no completed courses")       
        
add_student(students, "Peter")


def add_course(students: dict, name: str, courses: tuple):
    if name in students:
        
        course, grade = courses
        if grade == 0:
            return
        
        
        student_courses = students[name]
        
        found = False
        
        for i in range(len(student_courses)):
            existing_course, existing_grade = student_courses[i]
            
            if course == existing_course:
                found = True
                if grade > existing_grade:
                    student_courses[i] = (course, grade)   # as cahnging the copy of the tuple variable above wont change it.   
                grade = existing_grade
                break
            
        if not found:
            students[name].append((course, grade))
            
                
students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
print_student(students, "Peter")
# %%
arr = [1,2,3,2,4,5,1]
dict1 = {}
for item in arr:
    if item in dict1:
        dict1[item] += 1
    else:
        dict1[item] = 1
        
for key, value in dict1.items():
    if value == 1:
        print(key)
# %%
arr = [1,2,3,2,4,5,1]
unique = []
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count == 1 and arr[i] not in unique:                                                                          
        unique.append(arr[i])

print(unique)
# %%
arr = [1,2,3,2,4,5,1]
target = 6
seen = {}
for i in range(len(arr)):
    diff = target - arr[i]
    
    if diff in seen:
        print([seen[diff], i])
        
    seen[arr[i]] = i
    
print(seen)
# %%
# Armstrong Number

num = 153

sum = 0

num_str = str(num)
power = len(num_str)
for num_ind in num_str:
    sum += int(num_ind) ** power
    
if sum == num:
    print("Armstrong Num")
else:
    print("Not armstrong number")
    
# If the sum of the individual number each power to the length of given number is equal to the given num, its armstrong number
# %%
# write a program to print the duplicate characters in a string? ( language is optional )

str1 = 'aabbchgw'

i = 0
str = ''.join(sorted(str1))
while i < len(str):
    count = 1
    while i + count < len(str) and str[i] == str[i+count]:
        count += 1
        
    if count > 1:
        print(str[i],",", count)
        
    i += count
    
# Sort → Scan → Count → Print → Skip        
# %%
arr = [10, 5, 2, 7, 1, -10]
maxsum = 0
for i in range(len(arr)):
    
    sum = 0

    for j in range(i, len(arr)):
        sum += arr[j]
        
        if maxsum < sum:
            maxsum = sum 
        
print(maxsum)

# %%
# For each char in a string, print the count of its occurrences.

str = "aaabb"
str = ''.join(sorted(str))
i = 0
while i < len(str):
    count = 1

    while i + count < len(str) and str[i] == str[i+count]:
        count += 1
        
    print(str[i], count)
    
    i += count

# %%
# Longest non-repeating-character substring.

str = "aaabbcdef"
i = 0
char_set = set()
left = 0
maxlen = 0
for i in range(len(str)):
    while str[i] in char_set:
        char_set.remove(str[left])
        left += 1
        
    char_set.add(str[i])
    
    current_len = i-left+1
    
    if current_len > maxlen:
        maxlen = current_len
        
print(maxlen)
# %%
str = "aaabbcdef"
i = 0
char_set = []
left = 0
maxlen = 0
while i < len(str):
    if str[i] in char_set:
        char_set.pop(0)
        left += 1
        
    else:
        char_set.append(str[i])
        current_len = i-left+1
        
        if current_len > maxlen:
            maxlen = current_len
    
    i+= 1

    
print(maxlen)
# %%
# Max subarray sum in an integer array.

arr = [2, 3, -8, 7, -1, 2, 3]


def maxSubarraySum(arr):
    max_sum = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum
            
print(maxSubarraySum(arr))
            
# To check every subarray, u need to start from ith pos and go till end of the array.
# %%
array = [2, 3, -8, 7, -1, 2, 3]

first_ele = array[0]
max_sum = array[0]
for i in range(1, len(array)):
    if first_ele + array[i] > array[i]:
        first_ele += array[i]
    else:    
        first_ele = array[i]
        
    if first_ele > max_sum:
        max_sum = first_ele
        
print(max_sum)
    
# %%
'''
 1

 1 2 1

 1 2 3 2 1
'''
n = 3
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    for k in range(j-1, 0, -1):
        print(k, end=" ")
    print()

# %%

a = [7, 4, 3, 2, 8, 2, 4, 3, 7, 1]  
item = set()
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[j] == a[i]:
            count += 1
                
        if count > 1 and a[i] not in item:
            item.add(a[i])
            print(a[i])
        
        
        
# %%
a = [7, 4, 3, 2, 8, 2, 4, 3, 7, 1, 2]  
seen = set()
printed = set()

for item in a:
    if item in seen and item not in printed:
        print(item)
        printed.add(item)   
    else:
        seen.add(item)
# %%
a = [7, 4, 3, 2, 8, 2, 4, 3, 7, 1, 2]  
first_time = set()
dups = set()

for item in a:
    if item not in first_time:
        first_time.add(item)
    else:
        dups.add(item)
        
for item in a:
    if item not in dups:
        print(item)
# %%
def sample_decorator(func):
    def wrapper():
        print("Starting")
        func()
        print("Ending")
    
    return wrapper

@sample_decorator
def greet():
    print("Greet function gets called.")
    
greet()
# %%

n = 11
'''

01010
00001
-----
00000
'''

if (n & 1):  # False
    print("Odd")
else:
    print('Even')

# %%

# Greater number between 2 without using ternary or conditional

a = 15
b = 10
signed_bit = (a-b) >> 31  # For positive - 0; negative - 1; when right shift on signed integer, if its positive sign - 0 gets filled, if its negative sign - 1 gets filled.

result = a - ((a - b) & signed_bit) # If a=10, b=5 : 5 & 0 = 0 -- 0101 & 0000 => 0000 => a - 0 => a => 10
                                    # If a=5, b=10 : -5 & 1 gives the same number : -5 => 5 - (-5) => 10 => b
print(result)
# %%

# Calculate 7n/8 without using division and multiplication operators

# 16/8 = 2 => 10000 >> 3 => 00010 = 2
n = 8

right_shift = n >> 3

print(n - right_shift)
# %%
n = "123"
int_values = 0
for item in n:
    value = ord(item) - 48
    int_values += value
    
print(int_values)

# %%
# palindrome without using extra space

n = 1234321

divisor = 1
while (n/divisor >= 10):
    divisor *= 10
    
trailing_num = n % 10
leading_num = n // divisor

if (trailing_num != leading_num):
    print("Not a palindrome")

n = (n % divisor)//10

divisor = divisor/100

print("Palindrome")

# %%
# Square of a number without using *, / and pow()

def square(n):
    result = 0
    for _ in range(n):
        result += n
    return result

print(square(5))
# %%

# Check if two numbers are equal without using arithmetic and comparison operators
a, b = 5, 5

if (a ^ b == 0):
    print("Same")
else:
    print("Not Same")
# %%
def parantheses():
    string = '(((())))'
    stack = []
    for element in string:
        if element == '(':
            stack.append('(')
        else:
            if not stack:
                return "Empty Stack"
            else:
                stack.pop()

    if stack:
        return "Unbalanced"
    else:
        return "Balanced"

print(parantheses())

def without_stack():
    string = ')('
    stack_counter = 0
    for ele in string:
        if ele == '(':
            stack_counter += 1
        else:
            stack_counter -= 1
           
        if stack_counter < 0:
             return "Unbalanced"

    if stack_counter == 0:
        return "Balanced"
    else:
        return "Unbalanced"
    

print(without_stack())

# %%

expression = "5 1 2 + 4 * + 3 -"
print(postfix_eval(expression))

def string_to_int(value):
    result = 0

    for ele in value:
        result = (result * 10) + (ord(ele) - ord('0'))

    print(type(result))
    return result
print(string_to_int("48"))

str = "REVERSE"
string1 = list(str)

for ele in string1:
    