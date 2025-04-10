class Node:                    # A node has 2 components: Data and Next pointer, pointing successive nodes
    def __init__(self, data):
        self.data = data
        self.next = None 
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, data):
        start_node = Node(data)
        start_node.next = self.head
        self.head = start_node
        
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        
    def print_list(self):
        start = self.head
        while start:
            print(start.data, end="->")
            start = start.next
        print('None')
        print()
            
        
ll = LinkedList()
ll.prepend(10)
ll.prepend(20)

ll.append(30)
ll.append(40)
ll.print_list()
