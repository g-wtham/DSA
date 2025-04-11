# Insertion

'''
    50 -> data
    ||
   /  \
 30   60 -> data
(left) (right)
'''

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        
def insert(root, key):       # Called root parameter, since we START from root node whenever we try to insert and look for values which is lower or higher than the root node, that starting point is `root node`, so for insertion, a starting point is necessary to see where to insert the value
    if root is None:
        return Node(key)     # If there is no root node, pass the key into the Node class and return it as root node
    
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
        
    return root           # This returns the original root (the node with data 50), but now with its left pointer updated to point to the new node.

 
root = None               # Initialize to None, so a root node is created first                    
root = insert(root, 50)  
root = insert(root, 30)
root = insert(root, 70)   

print(root.left.data, root.data, root.right.data)
        
        
        