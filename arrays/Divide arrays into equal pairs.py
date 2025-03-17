'''
Divide Array Into Equal Pairs

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false
'''

nums = [3,2,3,2,2,2]

def equal_pairs(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for count in freq.values():
        if count % 2 != 0:
            return False
        
    return True

print(equal_pairs(nums))

'''
The function runs two separate **O(n) loops** (counting + checking), not nested loops, so the total time complexity is **O(n), not O(n²).** 
'''



