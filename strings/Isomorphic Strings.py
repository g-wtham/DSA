s = "egg"
t = "add"

def isomorphic_string(s, t):
    map_ch1 = {}
    map_ch2 = {}

    if len(s) != len(t):
        return False

    for ch1, ch2 in zip(s, t):
        if ch1 in map_ch1 and map_ch1[ch1] != ch2:
            return False
        if ch2 in map_ch2 and map_ch2[ch2] != ch1:
            return False
    
        map_ch1[ch1] = ch2
        map_ch2[ch2] = ch1

    return True

print(isomorphic_string(s, t))