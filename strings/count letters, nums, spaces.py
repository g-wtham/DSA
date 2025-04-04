input = input()

letters = spaces = numbers = special = 0

for char in input:
    if char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z':
        letters += 1
    elif char == ' ':
        spaces += 1
    elif char >= '0' and char <= '9':
        numbers += 1
    else:
        special += 1

print("Letters: ", letters)
print("spaces", spaces)
print("numbers", numbers)
print("special", special)