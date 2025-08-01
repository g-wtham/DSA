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
# %%
class Computer:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    
c1 = Computer("Gowtham", 12)
c2 = Computer("Ravi", 14)

print(c1)  # Prints the object memory address and not properties unless specified using . operator
 
print(c1.name)
print(c2.name)

print(c1.age)
print(c2.age)

class Computer2:
    def __init__(self) -> None:
        self.name = "Without Parameters"
        
withoutParameter = Computer2()

print(withoutParameter)
print(withoutParameter.name)


# %%

## Obj compare

class Computer:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def compare(self, other_obj):
        if self.age == other_obj.age:
            return True
        else:
            return False
        
        
computer1 = Computer("Gowtham", 12)
computer2 = Computer("Ravi", 13)

if computer1.compare(computer2):
    print("They are same")
else:
    print("They are not same")
# %%
class Computer:
    class_variable_wheels = 5
    
    def __init__(self) -> None:
        self.model = "BMW"
        self.petrol = 5
        
c1 = Computer()
c2 = Computer()

print("c1 obj: " ,c1.model, c1.petrol, "c2 obj: ", c2.model, c2.petrol)
print("Class Variable: ")
print(c1.class_variable_wheels)
print(Computer.class_variable_wheels)


# %%
'''
Variable Types - 
    i. Static(Class) variable;
   ii. Instance variable 
   
Method Types - 
    i. Instance methods
        - Accessors
        - Mutators
    ii. Class methods
    iii. Static methods
'''

class School:
    class_school_name = "Trust"
    
    def __init__(self) -> None:
        self.model = "BMW"
        self.petrol = 5

    def accessors(self):
        return self.model
    
    def mutators(self, value):
        self.model = value
        
    # To create a class method
    
    @classmethod
    def school_name(cls):
        return cls.class_school_name
    
    # Static Method - not related to class or instance variable
    
    @staticmethod
    def info():
        print("This is static method - not class method or instance method")
        
    
c1 = School()
c2 = School()
c3 = School()

print(c1.accessors())
c2.mutators("Audi")

print("Model Name: ", c2.model)
print(School.school_name())

School.info()
# %%
class Student:
    def __init__(self, name, class_name) -> None:
        self.name = name
        self.class_name = class_name
        self.laptop = self.Laptop()
    
    class Laptop:
        def __init__(self) -> None:
            self.laptop = "HP"
            
Student.Laptop().laptop  # Direct subclass calling

l1 = Student("gowtham", 12)  # Instance of a class
laptop1 = l1.laptop # Laptop 1

print("Subclass object property: ",laptop1.laptop)

l1 = Student('a', 12)
laptop_class = l1.Laptop()
print(laptop_class.laptop)
# %%
class Test:
    class_variable = 0                  # static variable (belongs to the class)

    
    def __init__(self):                 # instance method 
        
        instance_variable = 0           # local variable (belongs to a method)
        
        self.name = instance_variable   # instance variable
        
# Instance variable can be created at runtime and doesnt need explicitly mentioning it, rather than like in JAVA
# %%

class Bank:
    def __init__(self):
        self.__balance = 0
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
    
bank = Bank()
bank.deposit(1000)
bank.deposit(1000)
print(bank.get_balance())      
# %%

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car Started")
        
c = Car()
c.start()


# c.start() => Car.start(c)
# where, c = self
# %%
class Animal:
    def talk(self):
        print("Animal speaks")
        
class Lion(Animal):
    def speak(self):
        print("Lion speaks")
        
lion = Lion()
lion.speak()
lion.talk()
# %%
class Animal:
    def __init__(self):
        print("Animal Constructor")
        
    def talk(self):
        print("Animal speaks")
        
class Lion(Animal):
    def speak(self):
        print("Lion speaks")
        
lion = Lion()
lion.talk()
lion.speak()

# %%
