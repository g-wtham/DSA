password1=[1,4,4,3,2,6]

keypad = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

def get_pos(number):
    for i in range(3):
        for j in range(3):
            if keypad[i][j] == number:
                return (i, j)

def time2(password):
    time = 0
    for i in range(len(password)):
        if i==0:
            time += 1
        
        elif password[i-1] == password[i]:
            continue
        
        else:
            r1, c1 = get_pos(password[i-1])
            r2, c2 = get_pos(password[i])
            
            if abs(r1-r2) + abs(c1-c2) == 1:
                time += 1
            else:
                time += 2
            
    return time
        
    
print(time2(password1))
        
    
            

        
        
            
        