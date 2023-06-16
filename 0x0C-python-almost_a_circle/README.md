0x0C. Python - Almost a circle
Python OOP

Import
Exceptions
Class
Private attribute
Getter/Setter
Class method
Static method
Inheritance
Unittest
Read/Write file

args and kwargs
Serialization/Deserialization
JSON


*args and **kwargs in python*

In Python, *args and **kwargs are special syntax used to pass a variable number of arguments to a function. Here's a brief overview of *args and **kwargs:
*args: The *args syntax is used to pass a variable number of non-keyworded arguments to a function. It allows you to pass any number of arguments to a function, and those arguments will be wrapped up in a tuple. You can then iterate over the tuple to access each argument.
**kwargs: The **kwargs syntax is used to pass a variable number of keyworded arguments to a function. It allows you to pass any number of keyword arguments to a function, and those arguments will be wrapped up in a dictionary. You can then access the values of the dictionary using the keys.


def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('yasoob','python','eggs','test')

 *args and **kwargs are not required to be named as such, but the * and ** symbols are necessary to indicate that the function should accept a variable number of arguments.

json — JSON encoder and decoder
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. In Python, the json module provides functionality to encode and decode JSON data. The json module provides two methods for encoding Python objects as JSON data: json.dumps() and json.dump(). The json.dumps() method serializes Python objects to a JSON formatted string, while the json.dump() method serializes Python objects to a JSON formatted file. Similarly, the json module provides two methods for decoding JSON data into Python objects: json.loads() and json.load(). The json.loads() method deserializes a JSON formatted string to a Python object, while the json.load() method deserializes a JSON formatted file to a Python object.
The json module also provides two classes for encoding and decoding JSON data: JSONEncoder and JSONDecoder. The JSONEncoder class is used to encode Python objects as JSON data, while the JSONDecoder class is used to decode JSON data into Python objects. These classes can be subclassed to provide custom encoding and decoding behavior for specific Python objects.
