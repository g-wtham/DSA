def topKFrequent(nums, k):
        dict1 = {}
        for item in nums:
            if item in dict1:
                dict1[item] += 1
            else:
                dict1[item] = 1

        arr = []
        for key, value in dict1.items():
            arr.append([value, key])
        arr.sort(reverse=True)

        arr1 = []
        for i in range(k):
            arr1.append(arr[i][1])

        return arr1

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))