str1 = "CAT"
str2 = "ACT"

def anagram(s, t):
    if len(s) != len(t):
        return False

    freq_s = {}
    freq_t = {}

    for ch in s:
        if ch in freq_s:
            freq_s[ch] +=1
        else:
            freq_s[ch] = 1

    for ch in t:
        if ch in freq_t:
            freq_t[ch] +=1
        else:
            freq_t[ch] = 1

    return freq_t == freq_s


print(anagram(str1, str2)) 
        
