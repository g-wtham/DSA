'''
Input:

You’re given a string s consisting of * (frog) and | (stone), 
and an integer q – the number of queries. 
Each query provides two indices, l and r, and 
you need to count how many * appear between l and r (1-based).

|**|*|
1
1 5
'''
string = '|**|*|'
n = len(string)
l, r = 1, 5

prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + (1 if string[i] == '*' else 0)   # Offset from 0, since first element always 0 as there are no previous elements before it.
    
count = prefix_sum[r-1] - prefix_sum[l-1]
print(string, f' - Count of Stars from {l} to {r}:' ,count)
