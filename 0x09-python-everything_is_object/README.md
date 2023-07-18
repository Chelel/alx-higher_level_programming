0x09. Python - Everything is object
Python
Aliasing
Since variables refer to objects, if we assign one variable to another, both variables refer to the same object:

>>> a = [1, 2, 3]
>>> b = a
>>> a is b
True

*Immutable vs Mutable types*
bjects can be classified as either mutable or immutable. Mutable objects are those that allow you to change their value or data in place without affecting the object's identity. In contrast, immutable objects don't allow this kind of operation. You'll just have the option of creating new objects of the same type with different values. Some examples of immutable objects in Python include integers, floats, booleans, strings, and tuples. Examples of mutable objects include lists, dictionaries, and sets.

