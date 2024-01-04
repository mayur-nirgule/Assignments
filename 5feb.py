'''Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable ex
What is Class:
In Python every thing is an object. To create objects we required some Model or Plan
or Blue print, which is nothing but class.
We can write a class to represent properties (attributes) and actions (behaviour) of
object.
Properties can be represented by variables
Actions can be represented by Methods.
 Hence class contains both variables and methods.
 class Student:
ex:
 def __init__(self):
 self.name='durga'
 self.age=40
 self.marks=80

def talk(self):
 print("Hello I am :",self.name)
 print("My Age is:",self.age)
 print("My Marks are:",self.marks)

What is Object:
Pysical existence of a class is nothing but object. We can create any number of objects for
a class.
Syntax to Create Object: referencevariable = classname()
Example: s = Student()

2)The four pillars of object-oriented programming (OOP) are:

1. **Encapsulation:**
   - Encapsulation involves bundling the data (attributes) and the methods (functions) that operate on the data into a single unit known as a class.
   - It restricts access to some of the object's components, preventing the direct modification of internal state.

2. **Inheritance:**
   - Inheritance is a mechanism that allows a new class (subclass or derived class) to inherit properties and behaviors from an existing class (base class or parent class).
   - It promotes code reusability and establishes a relationship between classes.

3. **Polymorphism:**
   - Polymorphism allows objects of different classes to be treated as objects of a common base class.
   - It enables a single interface to represent different types or forms (methods or operations) and allows for code flexibility.

4. **Abstraction:**
   - Abstraction involves simplifying complex systems by modeling classes based on the essential properties and behaviors, while ignoring unnecessary details.
   - It provides a way to provide a simple interface to the user and hide the complexities of the implementation.

These four pillars together provide a framework for designing and organizing code in a way that promotes modularity, flexibility, and maintainability. They are fundamental principles that guide the design and implementation of object-oriented systems.

3)
In short, the `__init__()` function in Python is a special method in a class used to initialize the attributes of an object when it is created. It is automatically called when an object is instantiated from a class, allowing you to set the initial state of the object. This method is commonly known as the constructor, and it helps in organizing and customizing the properties of each instance.


4)In short, `self` is used in object-oriented programming to represent the instance of a class within its methods. It allows access to instance variables and methods, distinguishing between different instances and facilitating instance-specific operations. Using `self` is a convention that enhances code clarity and readability in Python and many other object-oriented languages.


5)In short, inheritance in object-oriented programming allows a new class to inherit properties and behaviors from an existing class, fostering code reuse. There are three main types:

1. **Single Inheritance:** Child class inherits from one parent class.
   - Example: `class Dog(Animal):`

2. **Multiple Inheritance:** Child class inherits from more than one parent class.
   - Example: `class Bird(Flyable, Swimmable):`

3. **Multilevel Inheritance:** Involves a chain of inheritance with multiple levels.
   - Example: `class Dog(Mammal):`

Inheritance facilitates the creation of a hierarchy of classes, promoting modularity and extensibility in code design.