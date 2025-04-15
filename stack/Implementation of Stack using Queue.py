from queue import Queue


# LIFO - Stack; FIFO - Queue
# So, we are using FIFO to do LIFO
# FIFO : [1,2,3,4] -> 1, 2
# Using queue: loop till size - 1 times, so last added element comes to the first position, after that using POP, it takes the element at first position. 

class StackusingQueue:
    def __init__(self):
        self.q = Queue()

    def push(self, value):
        s = self.q.qsize()

        self.q.put(value)
        for _ in range(s):
            self.q.put(self.q.get())

    def pop(self):
        n = self.q.get()
        return n
    
    def top(self):
        return self.q.queue[0]
    
    def size(self):
        return self.q.qsize()
    
stackUsingQueue = StackusingQueue()
stackUsingQueue.push(10)
stackUsingQueue.push(20)
stackUsingQueue.push(30)
print(stackUsingQueue.pop())
print(stackUsingQueue.top())
print(stackUsingQueue.size())