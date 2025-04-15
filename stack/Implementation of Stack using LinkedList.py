# For a ll, u need a node with data and next pointer
# Since it's a stack, which is LIFO, the current element's next pointer should point towards previous element (or previous top element)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None        # Actually, the next pointer works like previous pointer here!

class StackUsingLL:
    def __init__(self):
        self.top = None        # Since there are no elements initially, the top of the stack is NONE, which need to be explicitly mentioned orelse defining using other function would lead to errors, if that function wasnt called everytime the node is created

    def is_empty(self):
        return self.top is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top  # Previous element pointing here 
        self.top = new_node
        return new_node.data

    def pop(self):
        if self.is_empty():
            return "Empty Stack"
        
        top_ele = self.top.data
        self.top = self.top.next    
        return top_ele
    
    def peek(self):
        if self.is_empty():
            return "Empty Stack"
        
        return self.top.data
    
    def display(self):
        if self.is_empty():
            return "Empty Stack"
        
        current = self.top
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

stackLL = StackUsingLL()
print(stackLL.push(10))
print(stackLL.push(20))
print(stackLL.pop())
print(stackLL.peek())
stackLL.display()
