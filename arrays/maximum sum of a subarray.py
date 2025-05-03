arr = [2, 3, -8, 7, -1, 2, 3]

def subarray_sum_1(arr):
    result = arr[0]
    maxEnd = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > maxEnd + arr[i]:
            maxEnd = arr[i]
        else:
            maxEnd = maxEnd + arr[i]

        if maxEnd > result:
            result = maxEnd

    return result

print(subarray_sum_1(arr))

def subarray_sum_2(arr):
    result = arr[0]
    maxEnd = arr[0]

    for i in range(1, len(arr)):
        maxEnd = max(maxEnd + arr[i], arr[i])
        result = max(result, maxEnd)

    return result

print(subarray_sum_2(arr))

def subarray_sum_3(arr):
    current_result = arr[0]
    final_result = arr[0]
    start = end = temp_start_new_arr = 0

    for i in range(1, len(arr)):
        if arr[i] > current_result + arr[i]:
            current_result = arr[i]
            temp_start_new_arr = i

        else:
            current_result += arr[i] 

        
        if current_result > final_result:
            final_result = current_result
            start = temp_start_new_arr
            end = i

    return final_result, arr[start:end+1]

print(subarray_sum_3(arr))

