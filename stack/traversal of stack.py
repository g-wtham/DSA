from queue import LifoQueue

stack = LifoQueue()

def stack_traversal(stack):
    if (stack.empty()):
        return          # if stack is empty, return the function (termination point)
    
    x = stack.get()
    
    print(x, end=" ")
    
    stack_traversal(stack)
    
    stack.put(x)
    
stack.put(10)
stack.put(20)
stack.put(30)

stack_traversal(stack)