# With & Without constructor difference - Classes and Objects

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Node2:
    def node_func(self, data):
        self.data = data
        self.next = None

node = Node(10) 
    
node2 = Node2()
node2.node_func(10)

print(node.data)
print(node2.data)

'''
Node is just the blueprint.
node is the actual thing (object/backpack) with stuff inside.

Only real objects store actual data, not the blueprint. Functions doesnt store data.

In Python, functions are also objects.
But they don’t have a built-in way to remember data unless you manually attach stuff.

def greet():
    print("hi")

greet.name = "hello-fn"  --> attaching data manually
print(greet.name) 

In contrast, objects made from classes are designed to store data. That's their whole job.

Example: Pizza Shop Analogy
🧑‍🍳 make_pizza() = a function. It’s the act of making pizza.

🍕 pizza = Pizza() = an object. It’s the pizza you made.
'''