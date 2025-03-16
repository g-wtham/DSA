strs = ["flower","flow","flight"]

def common_prefix(strs):
    prefix = ""  # the empty string does exist initially, but it's visually empty
    first_word = strs[0]

    for i in range(len(first_word)):
        char = first_word[i]
        for str in strs[1:]:
            if i >= len(str) or char != str[i]: 
                return prefix
        
        prefix += char
    
    return prefix

print(common_prefix(strs))