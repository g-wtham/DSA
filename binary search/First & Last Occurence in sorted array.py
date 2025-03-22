def first_and_last(nums, target):
    def last_func(nums, target):
        last = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    last = mid
                left = mid + 1                    

            else:
                right = mid - 1

        return last

    def first_func(nums, target):
        first = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] >= target:
                if nums[mid] == target:
                    first = mid
                right = mid - 1

            else:
                left = mid + 1

        return first

    return [first_func(nums, target), last_func(nums, target)]