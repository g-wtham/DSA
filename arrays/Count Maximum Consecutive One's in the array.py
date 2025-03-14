prices = [1, 1, 0, 1, 1, 1]

max_count = 1
count = 1
for i in range(len(prices)-1):
    if prices[i] != prices[i+1]:
        count = 1
    else:
        count += 1
    
    max_count = max(max_count, count)
        
print(max_count)