0x0C-python-almost_a_circle

args and **kwargs

*args and **kwargs are mostly used in function definitions. *args and **kwargs
allow you to pass a variable number of arguments to a function.
What does variable mean here is that you do not know before hand that how many arguments
can be passed to your function by the user so in this case you use these two keywords.
*args is used to send a non-keyworded variable length argument list to the function

**kwargs allows you to pass keyworded variable length of arguments to a function.
You should use **kwargs if you want to handle named arguments in a function.


json — JSON encoder and decoder

JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627)
and by ECMA-404, is a lightweight data interchange format inspired by
JavaScript object literal syntax

import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(json.dumps("\"foo\bar"))
"\"foo\bar"
print(json.dumps('\u1234'))
"\u1234"
print(json.dumps('\\'))
"\\"
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
{"a": 0, "b": 0, "c": 0}
from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()
'["streaming API"]'
