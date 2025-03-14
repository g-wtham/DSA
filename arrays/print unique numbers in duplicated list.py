# Bruteforce

arr = [1, 1, 2, 5, 5, 6, 9, 9]

n = len(arr)
unique = []

for i in range(n):
    if arr[i] not in unique:
        unique.append(arr[i])
    
print(unique)

# Optimal 

n1 = len(arr)
seen = set()

for item in arr:
    if item not in seen:
        seen.add(item)

print(seen)