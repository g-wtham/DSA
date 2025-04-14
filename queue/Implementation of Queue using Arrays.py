class Queue_using_arrays:
    def __init__(self, n):
        self.capacity = n
        self.array = [None] * n
        self.end = -1
        self.start = -1
        self.current_size = 0
        
    def push(self, item):
        if self.start and self.end == -1:
            self.start = self.end = 0
            self.array[self.end] = item
            self.current_size += 1
            
        elif self.current_size == self.capacity:
            return "Can't push"
        
        elif self.current_size < self.capacity:
            self.end = (self.end + 1) % self.capacity
            self.array[self.end] = item
            self.current_size += 1
            
        else:
            self.end = (self.end + 1) % self.capacity
            self.array[self.end] = item

            
    def pop(self):
        if self.current_size == 0:
            return
        
        elif self.current_size == 1:
            cpy_pop = self.array[self.start]
            self.array[self.start] = None
            self.start = self.end = -1
            self.current_size = 0
            return cpy_pop
            
        else:
            cpy = self.array[self.start]
            self.array[self.start] = None
            self.start = (self.start+1) % self.capacity
            self.current_size -= 1
            return cpy
        
    def peek(self):
        if self.current_size == 0:
            return "Empty"
        
        return self.array[self.start]

        
        
queue = Queue_using_arrays(4)
print(queue.array)
queue.push(20)
queue.push(30)
queue.push(40)
queue.push(70)
print(queue.array)
print(queue.pop())
print(queue.pop())
print(queue.array)
print(queue.current_size)
print(queue.pop())
print(queue.array)
print(queue.peek())
print(queue.pop())
print(queue.array)
print(queue.peek())
