def f(i, N):
    if i > N:
        return 
    print("Gowtham")
    f(i+1, N)
    
N = 5
f(1, N)


N=10
def num3(i, N):
    if i > N:
        return
    print(i)
    num3(i+1, N)
    
num3(1, N)

N = 10
def num(N):
    if N==0:
        return
    num(N-1)
    print(N)
    
num(N)

N = 10
def num2(N, i):
    if N==0:
        return
    print(N)
    num2(N-1, 1)
    
num2(10, 1)