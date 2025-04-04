time = int(input())
enter_arr = [7,0,5,1,3]
exit_arr = [1,2,1,3,4]

for _ in range(time):
    a = int(input())
    enter_arr.append(a)

for _ in range(time):
    b = int(input())
    exit_arr.append(b)

'''
enter - exit = present time
if enter is 0, reduce from previous     present time instead of the 0
'''
max_time = 0
present_time = 0
for i in range(time):
    if enter_arr[i] > 0:
        if present_time == 0:
            present_time = enter_arr[i] - exit_arr[i]
        else:
            present_time = present_time + enter_arr[i] - exit_arr[i]
    else:
        if present_time != 0:
            present_time = present_time - exit_arr[i]
    
    max_time = max(max_time, present_time)

print(max_time)