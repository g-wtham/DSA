class QueueUsingStack:
    def __init__(self):
        self.stack_in = []
        self.stack_out = [] 

    def push(self, value):
        self.stack_in.append(value)   

    def pop(self):
        if not self.stack_out:              # Empty list means FALSE, so to run this if condition, taking a NEGATION approach.. NOT FALSE -> TRUE;
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if not self.stack_out:
            return "Empty Stack"
         
        return self.stack_out.pop()         # [1,2,3] => Takes last element, place it at first => [3,2,1] => Pop method removes last element which is FIRST element [1]
    
    def peek(self):
        if not self.stack_out:              # Empty list means FALSE, so to run this if condition, taking a NEGATION approach.. NOT FALSE -> TRUE;
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if not self.stack_out:
            return "Empty Stack"
        
        return self.stack_out[-1]
    
    def size(self):
        return len(self.stack_in) + len(self.stack_out)
    

qus = QueueUsingStack()
print(qus.push(10))
print(qus.push(20))
print(qus.push(30))
print(qus.push(40))
print(qus.pop())
print(qus.pop())
print(qus.peek())
print(qus.size())

'''
Only the first pop had to move 3 items from stack_in → stack_out, which is O(n).

The next two pops just pop from stack_out → O(1) each.

So, over 3 pops, the total work = O(n), but average per pop = O(1) → That's amortized O(1).
'''