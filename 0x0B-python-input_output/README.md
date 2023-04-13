0x0B-python-input_output

 Reading and Writing Files
open() returns a file object, and is most commonly used with two positional arguments and one keyword argument: open(filename, mode, encoding=None)

>>>
f = open('workfile', 'w', encoding="utf-8")
The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

Predefined Clean-up Actions
Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed. Look at the following example, which tries to open a file and print its contents to the screen.

for line in open("myfile.txt"):
    print(line, end="")
The problem with this code is that it leaves the file open for an indeterminate amount of time after this part of the code has finished executing. This is not an issue in simple scripts, but can be a problem for larger applications. The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
After the statement is executed, the file f is always closed, even if a problem was encountered while processing the lines.

