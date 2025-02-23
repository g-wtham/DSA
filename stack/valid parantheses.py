'''
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.
'''
def isBalanced(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:  # If closing bracket
            
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()
            
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return not stack

print(isBalanced('[{}]'))