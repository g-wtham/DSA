# Uses set to store duplicates, as membership checking for set is O(1)

arr = [1, 1, 2, 5, 5, 6, 9, 9]

n1 = len(arr)
seen = set()
dup = set()

for item in arr:
    if item in seen:
        dup.add(item)
    else:
        seen.add(item)

print(dup)
