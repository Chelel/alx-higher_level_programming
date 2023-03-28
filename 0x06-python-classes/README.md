0x06. Python - Classes and Objects
Object Oriented Programming.
OOP is a computer programming model that organizes software design around data, or objects, rather than functions and logic.
This is a way of organizing your program which is to combine data and functionality and wrap it inside something called an object.
Classes and objects are the two main aspects of object oriented programming.
A class creates a new type where objects are instances of the class.

CLASSES.
Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of that type to be made.
Each class instance can have attributes attached to it for maintaining its state.
Class instances can also have methods (defined by its class) for modifying its state.

Create a Class
To create a class, use the keyword class:

Create a class named MyClass, with a property named x:

       	 class MyClass:
	       x = 5

Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)