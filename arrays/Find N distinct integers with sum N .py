N = 14

result = []
for i in range(1, N):
    result.append(i)
    
X = N - sum(result)
result.append(X)

print(result)
    