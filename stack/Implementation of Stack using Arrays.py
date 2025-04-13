class Stack:
    def __init__(self, n):
        self.capacity = n
        self.array = [None] * n
        self.top = -1
        
    def push(self, item):
        if self.top >= self.capacity-1:
            return "Stack if full"
        
        self.top += 1
        self.array[self.top] = item
        return self.array
    
    def pop(self):
        if self.top == -1:
            return "Stack is already empty"
        
        top_ele = self.array[self.top]
        self.array[self.top] = None
        self.top -= 1
        return top_ele

    
    def peek(self):
        if self.top == -1:
            return -1
        
        return self.array[self.top]
    
    def size(self):
        return self.top + 1
    
    
        
stack = Stack(10)
print(stack.array)
print(stack.push(10))
print(stack.push(20))
print(stack.push(30))
print(stack.pop())
print(stack.array)
print(stack.peek())
print(stack.size())