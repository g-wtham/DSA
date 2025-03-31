'''
Given a non-negative integer array Arr having size N. Each element of the array will carry a different
value. This means no two elements can have the same values.The candidate has to do this with minimal
changes in the original value of the elements, making every element as least as much value as it originally
had.
Find the minimum sum of all elements that can be set the array for:
Example 1:
Input
3 -> Value of N, represents size of Arr
2 -> Value of Arr[0]
2-> Value of Arr[1]
4-> Value of Arr[2]
'''

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

flag = 0
for i in range(N):
    for j in range(i+1, N):
        if arr[i] == arr[j]:
            arr[j] += 1
        if arr[j] < 0:
            flag = 1
            break
sum = 0
if flag == 1:
    print("Wrong Input")
else:
    for item in arr:
        sum += item
    print(arr)
    print(sum)