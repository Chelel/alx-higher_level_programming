0x05. Python - Exceptions

1. Syntax Errors
2. Exceptions

Syntax Errors
Syntax errors, also known as parsing errors, are perhaps the most common kind of
complaint you get while you are still learning Python:

>>>
while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax


Exceptions
Even if a statement or expression is syntactically correct,
it may cause an error when an attempt is made to execute it.
Errors detected during execution are called exceptions and are not unconditionally fatal