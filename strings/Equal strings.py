def strings(s: str) -> str:
    dict1 = {'*': 0, '#':0}
    for item in s:
        if item in dict1:
            if item == '*':
                dict1[item] += 1
            elif item == '#':
                dict1[item] += 1

    return dict1['*'] - dict1['#']

print(strings("****####"))