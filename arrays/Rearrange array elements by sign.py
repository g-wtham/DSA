nums = [3,1,-2,-5,2,-4]


def array_sign(nums):
    n = len(nums)
    pos = []
    neg = []

    for i in range(n):
        if nums[i]>0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])

    for i in range(n//2):    
        nums[2*i] = pos[i]
        nums[2*i+1] = neg[i]

    return nums

print(array_sign(nums))