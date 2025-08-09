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

def valid_paran():
    string = '{[()]}'
    stack = []
    pairs = { '(': ')', '{': '}', '[': ']' }
    for ele in string:
        if ele == '{' or ele == '(' or ele == '[':
            stack.append(ele)
        else:
            if not stack:
                return "Empty Stack"
            else:
                top = stack.pop()
                if pairs[top] != ele:
                    return "Unbalanced"


    if not stack:
        return "Balanced"
    else:
        return "Unbalanced"
    
print(valid_paran())

def postfix_eval(string):
    stack = []

    string_list = string.split()
    
    for ele in string_list:
        
        if ele.isdigit():
            stack.append(int(ele))
        else:
            b = stack.pop()
            a = stack.pop()

            if ele == '+':
                stack.append(a + b)

            elif ele == '-':
                stack.append(a - b)

            elif ele == '*':
                stack.append(a * b)

            elif ele == '/':
                stack.append(int(a/b))

    return stack[0]

    