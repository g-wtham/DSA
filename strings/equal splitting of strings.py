'''
stringses
n = 3
0-3
3-6
6-9
'''

word = input()

N = int(input())

if len(word) % N == 0:
    i = 0
    while i < len(word):
        print(word[i:i+N])
        i+=N

word1 = input()

N1 = int(input())

part = len(word1) // N1

if len(word1) % N1 == 0:
    i1 = 0
    while i1 < len(word1):
        print(word1[i1:i1+part])
        i1+=part