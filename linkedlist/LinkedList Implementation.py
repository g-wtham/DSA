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
        
    def deletion_at_start(self):
        temp = self.head
        if temp is not None:
            self.head = temp.next
            temp = None
            
    def deletion_at_end(self):
        temp = self.head
        if temp is not None:
            while temp.next.next:
                temp = temp.next
            temp.next = None
            
    def deletion_at_k_position(self, key):
        start = self.head
        if start is not None:
            if start.data == key:
                self.head = start.next
                return
            
            while start.next:
                if start.next.data == key:
                    start.next = start.next.next
                    break
                start = start.next
                
    def insertion_at_k_position(self, value, key):
        start = self.head
        count = 1
        while start:
            if count == key-1:
                insert_node = Node(value)
                insert_node.next = start.next 
                start.next = insert_node
                break
            start = start.next
            count += 1
            
        
ll = LinkedList()
ll.prepend(10)
ll.prepend(20)
ll.print_list()
ll.append(30)
ll.append(40)
ll.print_list()
ll.deletion_at_k_position(30)
ll.append(50)
ll.append(60)
ll.print_list()
ll.deletion_at_end()
ll.print_list()
ll.insertion_at_k_position(30, 3)
ll.print_list()
