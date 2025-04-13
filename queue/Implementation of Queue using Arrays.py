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
        
        elif self.current_size < self.capacity:
            self.end += 1
            self.array[self.end] = item
            self.current_size += 1
            
        else:
            self.end = (self.end + 1) % self.capacity
            self.array[self.end] = item

            
    def pop(self):
        if self.start and self.end == -1:
            return
        
        elif self.current_size < self.capacity:
            cpy = self.start
            self.array[self.start] = 0
            self.start += 1
            return self.array[cpy]
            
        else:
            self.start = (self.start + 1) % self.capacity
            cpy = self.start
            self.array[self.start] = None
            self.start += 1
            return self.array[cpy]

        
    def peek(self):
        return self.array[self.start]
        
        
queue = Queue_using_arrays(10)
print(queue.array)
queue.push(20)
queue.push(30)
print(queue.array)
print(queue.current_size)
print(queue.peek())
queue.pop()
print(queue.array)

