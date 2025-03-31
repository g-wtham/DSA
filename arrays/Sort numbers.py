'''
Q1. Airport security officials have confiscated several items of the passenger at the security checkpoint. All
the items have been dumped into a huge box(array). Each item possessed a certain amount of risk(0,1,2).
Here is the risk severity of the item representing an array[] of N number of integer values. The risk here is to
sort the item based on their level of risk values range from 0 to 2.

Example 1:

Input:
7 ----- Value of N
[1,0,2,0,1,0,2] -> Element of arr[0] to arr[N-1], while input each element is separated by new line

Output:
0 0 0 1 1 2 2 -> Element after sorting based on the risk severity.
'''
arr = [1,0,2,0,1,0,2]
count_0 = 0
count_1 = 0
count_2 = 0

for i in range(len(arr)):
    if arr[i] == 0:
        count_0 += 1
    elif arr[i] == 1:
        count_1 += 1
    else:
        count_2 += 1
        
for x in range(count_0):
    arr[x] = 0
    
for y in range(count_0, count_0+count_1):
    arr[y] = 1
    
for z in range(count_0+count_1, len(arr)):
    arr[z] = 2
    
print(arr)
    
