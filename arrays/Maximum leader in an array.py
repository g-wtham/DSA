arr = [10, 22, 12, 3, 0, 6]

# Initial bruteforce approach
# Issues: checks the entire array repeatedly in ele set(), inefficient extra space
rightmost = arr[-1]
seen = set()
ele = set()

for i in range(len(arr)-2, 0, -1):
    if arr[i] > rightmost:
        seen.add(arr[i])
        for item in seen:
            ele.add(arr[i])

print(list(ele)[::-1]+[rightmost])

# 2nd iteration
arr = [10, 22, 12, 3, 0, 6]

def leadersInArray(arr):
    rightmost = arr[-1]
    leaders = [rightmost]
    for i in range(len(arr)-2, -1, -1): # to include 0th index also, -1 as end range, as end is exclusive
        if arr[i] > rightmost:
            rightmost = arr[i]
            leaders.append(arr[i])
            
    return leaders[::-1]

print(leadersInArray(arr))
        


