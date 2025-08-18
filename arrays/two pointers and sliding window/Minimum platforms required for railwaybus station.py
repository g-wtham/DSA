arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

platform_needed = 0
maximum_platform_needed = 0
arrival_ptr = 0
depature_ptr = 0

arr.sort()
dep.sort()

while arrival_ptr < len(arr) and depature_ptr < len(dep):
    if arr[arrival_ptr] < dep[depature_ptr]:
        platform_needed += 1
        arrival_ptr += 1
    else:
        platform_needed -= 1
        depature_ptr += 1
        
    maximum_platform_needed = max(maximum_platform_needed, platform_needed)
    

print(maximum_platform_needed)

# %%

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

arr.sort()
dep.sort()

n = len(arr)
result = 0

for i in range(n):
    cnt = 1
    for j in range(n):
        if i != j:
            if arr[i] >= arr[j] and arr[i] <= dep[j]:
                cnt += 1
                
    result = max(result, cnt)    

print(result)
# %%
