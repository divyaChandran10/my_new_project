The World as Objects:
What is OOP?
Why do we need OOP?
What is an Object, and what is a Class?
How does a Class look like in Python?
Tips for learning OOP.

Object-Oriented Programming (OOP)

→ It makes code more reusable and makes it easier to work with larger programs.
→ uses objects and classes in programming.
Class 
A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods.
To understand why we need class:
To track the number of dogs that may have different attributes like breed, age. If a list is used, the first element could be the dog’s breed while the second element could represent its age. Let’s suppose there are 100 different dogs, then how would you know which element is supposed to be which? What if you wanted to add other properties to these dogs?

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute
Create Class:

class Dog:
    pass
Objects
One of the popular approaches to solve a programming problem is by creating objects.
The object is an entity that has a state and behavior associated with it.
An object consists of :
State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.
To understand the state, behavior, and identity let us take the example of the class dog (explained above). 
The identity can be considered as the name of the dog.
State or Attributes can be considered as the breed, age, or color of the dog.
The behavior can be considered as to whether the dog is eating or sleeping.
Create an object:
obj = Dog()
Creating a class and object with class and instance attributes

class Dog:
  
    # class attribute
    attr1 = "mammal"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name

    # Method
    def speak(self):
        print("My name is {}".format(self.name))
  
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
  
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
  
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

# Accessing class methods
Rodger.speak()
Tommy.speak()


Inheritance
Inheritance is the capability of one class to derive or inherit the properties from another class. 
# parent class
class Person(object):
  
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
  
    def display(self):
        print(self.name)
        print(self.idnumber)
          
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
      
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
  
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
          
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
  
  
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
  
# calling a function of the class Person using its instance
a.display()
a.details()


Polymorphism
Polymorphism simply means having many forms. 
class Bird:
    
    def intro(self):
        print("There are many types of birds.")
  
    def flight(self):
        print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly.")
  
class ostrich(Bird):
  
    def flight(self):
        print("Ostriches cannot fly.")
  
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()



Output:

There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.

Encapsulation
Encapsulation is one of the fundamental concepts 
in object-oriented programming (OOP). It describes the idea of 
wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly
and can prevent the accidental modification of data. 
To prevent accidental change, an object’s variable can only be changed
by an object’s method. Those types of variables are known as private variables.

