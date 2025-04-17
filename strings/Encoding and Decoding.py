strings = ["hello", "world"]
def encode(strings):
    res = ""
    for str1 in strings:
        res += str(len(str1)) + '#' + str1
    return res

result = encode(strings)
def decode(result):
    res = []
    i = 0
    while i < len(result):
        j = i
        if result[j] != '#':
            j+=1
        length = int(result[i:j])
        res.append(result[j+1:j+length+1])
        i=j+length+1

    return res


print(encode(strings))
print(decode(result))