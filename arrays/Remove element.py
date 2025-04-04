'''
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
'''

def removeElement(nums, val):
    index = 0
    for item in nums:
        if item != val:
            nums[index] = item
            index += 1
    return index