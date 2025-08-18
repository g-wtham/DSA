array = [1,7,2,5,8]
target = 8

i = 0
j = len(array) - 1

array.sort()

while i < j:
    if (array[i] + array[i+1] + array[j]) < target:
        i += 1
    elif (array[i] + array[i+1] + array[j]) > target:
        j -= 1
    else:
        print("Possible")
        break
