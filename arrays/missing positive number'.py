arr = [3, 4, -1, 1]
n = len(arr)

def missing_positive(arr):
    i = 0
    while i < n:
        correct_pos = arr[i] - 1         # applicable to non-duplicate elements only 
        if 1 <= arr[i] <=n and  arr[i] != arr[correct_pos]:
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i] 
            # dont increment here by 1 as newly swapped value will have different positions, as now a[0] value will be different ie.. it will be the swapped value
        else:
            i+=1

    for i in range(n):
        if arr[i] != i+1:
            return i+1
        
    return n+1

print(missing_positive(arr))

'''
1. Initialize i=0 to start from 0th element
2. Till current ele is less than n (total_len), check if it is between 1 and N to assure it is positive num only and place the current element in its correct position, since the array is unsorted.
3. To get the correct position, as 0-based index, deduct 1 from the current element -> arr[i] - 1 -> 3-1 -> 2nd index for 3, which is correct position.
4. Now check if the current element and element at the correct position are different, if it is, swap them or else, just increment by one, to move to the next position and check this condition
5. Use 'if' to check and not 'while', because we only need to swap once, if we used while, we would be continuously swapping the same element, leading to infinite loop.
6. After swapping, iterate from 0 to n, if element at i, is not equal to index + 1, then it is different element or like, missing element, so return it..
7. If everything is equal, then the element after the last element is the missing one, so return i + 1
'''

'''
✅ Use while when swapping is involved (e.g., Cyclic Sort).
🚫 Don't use for when swaps change positions, because it blindly increments i.

Golden Rule:

If every element is processed exactly once, use for.
If some elements need to be processed multiple times before moving on, use while.
'''