def f(i, N):
    if i > N:
        return 
    print("Gowtham")
    f(i+1, N)
    
N = 5
f(1, N)