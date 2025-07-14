arr = 'XXV'
res = 0
i = 0
romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
while i < len(arr):
    if i+1 < len(arr) and romanMap[arr[i]] < romanMap[arr[i+1]]:
        res += romanMap[arr[i+1]] - romanMap[arr[i]]
        i += 1
    else:
        res += romanMap[arr[i]]
    
    i += 1

print(res)
