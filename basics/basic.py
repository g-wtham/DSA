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

# %%

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

def string_to_int(value):
    result = 0

    for ele in value:
        result = (result * 10) + (ord(ele) - ord('0'))

    print(type(result))
    return result
print(string_to_int("48"))

# %%

str = "REVERSE"
string1 = list(str)
n = len(string1)-1

for i in range(len(string1)//2):
    string1[n], string1[i] = string1[i], string1[n]
    n -= 1
    
print(''.join(string1))
    
# %%
def square(num):
    final = 0
    for _ in range(num):
        final += num
        
    return final

square(10)
# %%
num1 = 5
num2 = 5

if num1 ^ num2 == 0:
    print("Equal")
else:
    print("Not equal")
# %%
num2 = 52

if num2 & 1 == 1:
    print("Odd Number")
else:
    print("Even Number")
# %%
def max_element(a, b):
    signed_bit = (a - b) >> 31
    return a - (signed_bit & (a-b))

arr = [1, 5, 3, 4]
largest = arr[0]
for ele in arr:
    largest = max_element(largest, ele)
    
print(largest)

# %%

def factorial(n):
    # 2, 6, 12, ...
    
    fact = 1
    for i in range(2, n+1):
        temp_sum = 0
        for _ in range(i):
            temp_sum += fact
        
        fact = temp_sum 
    
    return fact

print(factorial(5))
        
# %%
def print_numbers(n):
    if n>1:
        print_numbers(n-1)
    print(n)    
    
print_numbers(5)
# %%
def multiply(a, b):
    result = 0
    for _ in range(b):
        result += a
        
    return result

print(multiply(15, 10))
# %%
# String Methods :

text = "   hello world\tthis is PYTHON 123\t\n"

print(dir(text))

print(text.lstrip())
print(text.lstrip())
print(text.strip())
print(text.strip().capitalize())
print(text.strip().title())
print(text.upper())
print(text.swapcase())

# swaps the alphabets case

test = 'Straße'
print(test.casefold())
print(test.lower())

print("text12".isalnum())
print("text".isalpha())
print("abc".isascii())

text2 = 'Ⅷ'
print(text2.isdecimal()) # checks only 0-9 numbers
print(text2.isnumeric()) # checks 0-9, roman numerals, and also fractions.
print(text2.isdigit())   # checks only 0-9 and fractions, no roman numerals.

text3 = "124"
print(text3.isdecimal(), text3.isnumeric(), text3.isdigit()) # true for all 

print('1test_3'.isidentifier())
# Returns false, becoz identifier should only contain A-Z, a-z, numbers (0-9) and underscore (_). It should not start with a number, starting with _ is allowed. Any other characters are invalid, like -, ;, emojis..

print('test-mode'.isidentifier()) # Returns false, as '-' shouldn't be in userdefined variable names

text4 = " "
print(text4.isspace())
text4 = ""
print(text4.isspace())

text5 = "ababab"
print(text5.count('ab')) # gets the count of the occurence of the substring given as parameter

print(text5.find("b")) # finds the FIRST occurence index position of the given substring
print(text5.find("c")) # If didnt found, returns -1, rather than ERROR.

print(text5.index("b")) # Same as find(), differs in exception handling

print(text5.index("c")) # raises error, if the substring is not found - "ValueError: substring not found". Program halts here and doesnt proceed. Use index(), if strict checking of the value is required, like you're sure about the value must exists, orelse don't proceed forward.

print(text5.rfind("b")) # returns the rightmost index position of the given substring if found. 

print(text5.rfind("c")) # Else, returns -1.

print(text5.rindex("b")) 

# print(text5.rindex("c"))

filename = "syllabus.pdf"
print(filename.endswith("pdf")) 

invoice_number = "23" # If invoice number needs to be certain digits we can fill it using zfill
print(invoice_number.zfill(10))
print(invoice_number.center(10, '-')) # beautification

print(invoice_number.replace('2', '4')) 

email = 'user@gmail.com'
print(email.partition('@')) # gives a tuple of partition by '@' symbol

csv_line = "apple,banana,cherry"
print(csv_line.split(','))

data = "Name\tAge\tCity"
print(data.expandtabs(10))

# Supports int, string, etc..

msg = "Hello {}, your OTP is {}"
print(msg.format("Yogesh", 123))

msg = "Hello {}, your OTP is {}"
print(msg.format("Yogesh", "123"))

# format map : uses dictionary

data = {
    "name": "Yogesh",
    "order_id": 12345,
    "status": "shipped"
}
template = "Hello, {name}! Your order ID is #{order_id} and the status is {status}."
print(template.format_map(data))

# To text censorship (or) do custom text encoding & decoding

bad_text = "This is damn bad!"
translation_table = str.maketrans({'d': '*', 'm': '@'})
print(bad_text.translate(translation_table))

# Cleaning multi-line feedback from users into single line
# Use - splitlines(), strip(), join()

feedback = """Great app!
   
Very useful.   

Will recommend to friends.
"""

lines = feedback.splitlines()
cleaned_lines = []
for line in lines:
    if line.strip():
        cleaned_lines.append(line.strip())
print(cleaned_lines)
print(" ".join(cleaned_lines))

# %%

# These return FALSE values. All empty string, 0 value, empty sequence data types, empty dict, None type 

print(bool([]))
print(bool(()))
print(bool({}))
print(bool(""))
print(bool(None))
print(bool(0))
print(bool(False))


class My_bool:
  def  __len__():
    return 0
    
bool_obj = My_bool.__len__()
print(bool(bool_obj))

# %%
x = 200
print(isinstance(x, int))

def radius(r):
  if not isinstance(r, (int, float)):
    raise TypeError("Invalid Input")
  return r
  

print(radius(12))
print(radius('12')) # gives error

# %%

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[2:4] = ["orange", "apple"]
print(thislist)

thislist.insert(2, "grape")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thistuple2 = {'name': 'Yogesh', 'age': 10}
thislist.extend (thistuple2)
print(thislist)

thislist3 = ["apple", "banana", "cherry"]
del thislist3[0]   # a python statement, doesnt return any value
print(thislist3)

thislist3 = ["apple", "banana", "cherry"]
removed_element = thislist3.pop(0)
print(removed_element)     # a list method, the popped value can be stored and returned
print(thislist3)

# List Comprehension : 
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# reverse() - regardless of the order, its just reverses the list
# sort(reverse = True) - sorts by descending order of the alphabets

# Copying of lists - 1. Using copy()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits2 = fruits.copy()
print(fruits2)

# 2. Using slicing operator 

fruits2 = fruits[:]
print(fruits2)

# 3. Using list() method

fruits3 = list(fruits)
print(fruits3)

# List Methods -> count(), index()

fruits = ["apple", "banana", "cherry", "apple", "apple"]
print(fruits.count("apple"))

# Returns 0, if not found

fruits = ["apple", "banana", "cherry", "apple", "apple"]
print(fruits.index("cherry"))

# Collections of data storing in python : Lists, Tuples, Sets, Dictionaries

tuple1 = ("apple1", ) # For one element, we should add comma orelse python won't consider it as a valid tuple -> tuple1 = ("apple") is incorrect

# Python Sets :

# Available methods : add(), update(), remove()

set1 = {1, True}
print(set1)

# cant access by index, as sets are unordered, hashable, unchangeable and unique values.
# the values can be modified like in lists in sets. 
thisset = {"apple", "banana", "cherry"}
for item in thisset:
    print(item)
    
thisset.update(set1)
print(thisset)

# Set uses hash function, so the order of insertion is not maintained while inserting the combining two items, each time the output varies by a lot.
list2 = [1,2,3]
thisset.update(list2)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)

thisset.discard("banana")
print(thisset)

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# Tuples dont have clear() method, list() and set() have .clear() method
# Deletion methods : del, remove, pop; pop method will remove a random value, so better off avoid using it for deletion in a set.

'''
&  - set intersection
| - set union
- -> set difference
^ - symmetric difference (keeps all values from A and B, but not the common values)

Using the symbols doesn't let us use it with OTHER DATA TYPES like lists, tuples, dict, etc.. Using the set methods will let us use the various set method like :

add() - adds a SINGLE element to the set
union() - can join two sets, returns a new set (|) as output
difference() - keeps the elements in set1 but not the ones in set2. 
intersection() - can join two sets with their common values, returns a new set (&) as output
symmetric_difference() - gives elements in two sets, but not the ones which are common.

All these methods return a new output. It does not updates the direct sets, to directly update the sets, we should use :

update() - Adds elements from another iterable to the current set.
difference_update()	- Removes all elements from the current set that are also in another set.
intersection_update() - Keeps only the elements that are common to both sets.
symmetric_difference_update() - Keeps all elements that are not in both sets.

For more : https://www.w3schools.com/python/python_sets_methods.asp
'''

math_class = {"John", "Alice", "Bob", "Charlie"}
science_class = {"Alice", "David", "Eva"}
history_class = {"Bob", "Frank", "Grace"}

math_class.add("Jona")
print(math_class)

students = ["John", "Kelly", "Olivia"]
math_class.update(students)
print(math_class)

new_class = math_class.intersection(science_class)
print(new_class)

new_class = math_class.difference(science_class)
print(new_class)

new_class = math_class.symmetric_difference(science_class)
print(new_class)

new_class = math_class.union(science_class)
print(new_class)

new_class = math_class | science_class # union
print(new_class)

new_class = math_class & science_class # intersection
print(new_class)

A = {1, 2, 3}
B = {3, 4, 5}
C = {1, 2, 3, 4, 5}
D = {6, 7, 8}

print(A.issubset(C))
print(C.issuperset(A))

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = {"orange", "apple", "banana", "microsoft"}

print(set1.issubset(set1))

# Dictionaries : 

# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

dict1 = dict(name = "Yogesh", age = 20, Status = True)
print(dict1)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.get("model")) # the key value should be quoted
print(thisdict.values())
print(thisdict.keys())
print(thisdict.items())

# To check if the key exists in the dictionary
if "year" in thisdict:
    print("Exists!")

# To update existing value
dict1.update({"name" : "arun"})

# To change a value :
dict1["age"] = 25     # since its outside dictionary, = should be used

# fromkeys() method = useful for quick dict initialization
keys = ['apple', 'banana', 'cherry']
x = dict.fromkeys(keys, 0)
print(x)

dict1.pop("name")
dict1.popitem()

# ---------------------
a = 5
b = 2
print(a) if a > b else print(b)
if a > b: print(a)

# %%

def prime(n):
    if n == 1:
        return "Not prime or composite"

    # no need to check with 1 and the number itself
    for i in range(2, n):
        if n % i == 0:
            return False

    return True   

prime(5)

# Efficient approach using square root - as finding one of the factors of a given number is enough
# Eg.. For 100 - 1,2,4,5,10 - as checking till 10 (it's square root will suffice), because one of the factors of 100 is within this range.

import math 

def prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

prime(15)
# %%

# Prime numbers till n 

def prime_numbers(n):
    nos = []
    if n <= 1:
        return False
    
    def is_prime(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
            
        return True

    for i in range(2, n+1):
        if is_prime(i):
            nos.append(i)

    return nos

print(prime_numbers(10))

def efficient_prime_numbers(n):
    prime_bool = [True] * (n+1)
    prime_bool[0] = prime_bool[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if prime_bool[i]:
            for i in range(2*i, n+1, i):
                prime_bool[i] = False

    primes = []
    for i in range(2, n+1):
        if prime_bool[i]:
            primes.append(i)

    return primes

print(efficient_prime_numbers(10))


# %%
num = 2192
rev_num = 0
while num > 0:
    last_digit = num % 10
    rev_num = rev_num * 10 + last_digit
    num = num//10

print(rev_num)

# %%

year = 2004
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("True")

else:
    print("False")

# %%

def find_largest_number(numbers):
  # Handle the edge case of an empty list
  if not numbers:
    return None 

  max_so_far = -float('inf')

  for item in numbers:
    if item > max_so_far:
      max_so_far = item

  return max_so_far

my_list = [17, 9, 42, 3, 28]
find_largest_number(my_list)

# %%

def fibonacci(num):
    
#     fib(0) = 0 
#     fib(1) = 1

#               fib(4)
#              /      \
#         fib(3)        fib(2)
#        /      \      /      \
#     fib(2)  fib(1)  fib(1)  fib(0)
#    /      \
# fib(1)  fib(0)
    
    if num == 0:
        return 0
    
    if num == 1:
        return 1

    return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(5))

# Time complexity = O(2^N) as the values grow exponentially

# To run in O(N) time complexity, we can use loops/iteration 

def fibonacci_with_loop(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b

    return b

print(fibonacci_with_loop(5))
# %%

def gcd(a, b):

    small_num = min(a, b)
    for i in range(small_num, 0, -1):
        if (a % i == 0 and b % i == 0):
            return i
        
print(gcd(20, 30))

# O(N) - time complexity, O(1) = space complexity

def gcd_optimized(a, b):
    while b != 0:
        a, b = b, (a%b)
    
    return a

print(gcd_optimized(20, 30))

# 20, 30 => 30, 20 => (20 smallest value, 10 remainder) => (20, 10) => (10, 0) => 10 is the GCD.
# O(log min(a, b)) - time complexity, O(1) = space complexity
# %%
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def factorial_with_loop(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial_with_loop(5))

# Time Complexity = O(N) for both
# Space Complexity = O(1) for iterative approach as ONLY the values hold constant value each time; O(N) for recursive approach

# %%

arr = [1,2,2,3,4,5,5]
result = []
for ele in arr:
    if ele not in result:
        result.append(ele)
        
print(result)

seen = set()
result = []
for ele in arr:
    if ele not in seen:
        result.append(ele)
        seen.add(ele)
print(result)

# %%
arr = [1,2,2,3,4,5,5]

i = 0
arr.sort()
for j in range(1, len(arr)):
    if arr[j] != arr[i]:
        i += 1
        arr[i] = arr[j]
        
print(arr[:i+1])

# %%
arr = [3,4,5,5,1,2,2]
i = 0
for j in range(len(arr)):
    if arr[j] not in arr[:i]:
        arr[i] = arr[j]
        i+=1
        
print(arr[:i])

# We are checking if the current element is not so far found till `i` elements, then place the current element in i.
# %%

# armstrong number

num = 155

def armstrong(num):
    num_str = str(num)
    n = len(num_str)
    total = 0
    for ele in num_str:
        total += int(ele) ** n
    return total == num 

print(armstrong(num))

# %%

from math import sqrt

def prime_numbers_bw(num):
    if num <= 1:
        return False
    
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
        
    return True

num = 10
result = []
for j in range(num):
    if prime_numbers_bw(j):
        result.append(j)
        
print(result)
    
# %%

def prime_number(num):
    if num <= 1:
        return False
     
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
        
    return True

def prime_num_range(num1, num2):
    result = []
    for j in range(num1, num2+1):
        if prime_number(j):
            result.append(j)
    
    return result

print(prime_num_range(3, 10))

# %%

a = '1010'
b = '1111'

def binary_str_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

print(binary_str_add(a, b))

# %%
num = 6
if num & 1 == 0:
    print("Even")
else:
    print("Odd") 
    
# %%

a,b = 12, 18

def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1
            
print(lcm(a, b))

# %%

a,b = 20, 28
def gcd(a, b):
    minimum = min(a, b)
    for i in range(minimum, 0, -1):
        if a % i == 0 and b % i == 0:
            return i 
        
print(gcd(a, b))

# %%

# Display All Prime Numbers from 1 to N
import math
def prime_using_sieve(n):
    if n < 2:
        return []

    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p <= int(math.sqrt(n)):
        for i in range(2*p, n+1, p):
            if is_prime[i]:
                is_prime[i] = False

        p += 1

    result = []
    for i, prime in enumerate(is_prime):
        if prime:
            result.append(i)

    return result

print(prime_using_sieve(10))


# %%
n = 2021
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("Leap")
else:
    print("Not leap year")

# %%

a , b = 100, 500

def optimized_check_armstrong(i):
    a = len(str(i))
    num = i
    total = 0
    while i != 0:
        digit = i % 10
        total += digit ** a
        i = i // 10

    return total == num


def check_armstrong(i):
    value = str(i)
    total = 0
    for char in value:
        total += int(char) ** len(value)
    return total == i

def print_armstrong_nums(a, b):
    for i in range(a, b+1):
        if optimized_check_armstrong(i):
            print(i, end=" ")   
    return 

print_armstrong_nums(a, b) 

# %%

# Neon number

n = 9
square = n ** 2
total = 0
while square != 0:
    last_digit = square % 10
    total += last_digit
    square = square // 10

if n == total:
    print("Neon Number")
else:
    print("Not neon number")

# %%

a = 'a'
vowels = 'aeiou'
if a in vowels:
    print("Vowel")
else:
    print("Consonant")

# %%
def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    return n * factorial(n-1)

# using loop

n = 5
print(factorial(n))
result = 1
for i in range(1, n+1):
    result = result * i
print(result)

# res = 1 * 1; res = 1 * 2; res = 2 * 3 = 6; res = 6 * 4 = 24; res = 24 * 5 = 120;

# %%
# Find the sum of all even Fibonacci numbers not greater than n.

n = 10
a, b = 0, 1
total = 0
while a <= n:
    if a % 2 == 0:
        total += a
    a, b = b, a+b

print(total) 

# %%

# Non repeating elements in an array

array_1 = [1, 5, 2, 1, 3, 5, 4]

freq_map = {}
for ele in array_1:
    if ele in freq_map:
        freq_map[ele] += 1
    else:
        freq_map[ele] = 1

result = []
for item, count in freq_map.items():
    if count == 1:
        result.append(item)

print(result)

# %%

# Non repeating element bruteforce

array_1 = [1, 5, 2, 1, 3, 5, 4]
result = []
for i in range(len(array_1)):
    picked_element = array_1[i]
    is_repeated = False

    for j in range(len(array_1)):
        if i != j and array_1[j] == picked_element:
            is_repeated = True
            break
    
    if not is_repeated:
        result.append(picked_element)

print(result)
# %%

# Valid Anagrams:

t1 = 'listen'
t2 = 'silen'

if len(t1) != len(t2):
    print("False")

t1_map = {}
for ele in t1:
    if ele in t1_map:
        t1_map[ele] += 1
    else:
        t1_map[ele] = 1


t2_map = {}
for ele in t2:
    if ele in t2_map:
        t2_map[ele] += 1
    else:
        t2_map[ele] = 1

print(t1_map == t2_map)

# %%

# Array rotation by k position

arr = [1,2,3,4,5]
k = 14

if k > len(arr):
    k = k % len(arr)

print(arr[k:] + arr[:k])
# %%
# 15. Longest Consecutive Subsequence 

lcs_input = [100, 4, 200, 1, 1, 3, 2]
lcs_input.sort()
length = 1
max_len = 1
for i in range(1, len(lcs_input)):
    # handling edge cases
    if lcs_input[i] == lcs_input[i-1]:
        continue

    if abs(lcs_input[i]) - abs(lcs_input[i-1]) == 1:
        length += 1
    else:
        length = 1

    max_len = max(max_len, length)


print(max_len)


# %%

# %%


# %%

# %%

# %%

#%%
