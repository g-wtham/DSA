def frequencySort(s):
    dict1 = {}
    for char in s:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1

    def get_element(x):
        return x[1]

    sorted_list = sorted(dict1.items(), key=get_element, reverse=True)

    result = ""
    for key, value in sorted_list:
        result += key * value
    
    return result

s = "tree"
print(frequencySort(s))
