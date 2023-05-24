Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def investigate(async_iterator):
    """yield (y) to investigate (x) crude oil leakage"""  # track illigal pipe conduits.
    map(investigate, "yield")
    print("yield")

    
async_iterator = (y, x)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    async_iterator = (y, x)
NameError: name 'y' is not defined
async_iterator = (y = 78, x = 19)
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
async_iterator = (y := 78, x := 19)
print(async_iterator)
(78, 19)
print(async_iterator + ("yield"))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(async_iterator + ("yield"))
TypeError: can only concatenate tuple (not "str") to tuple
print(async_iterator ("yield"))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(async_iterator ("yield"))
TypeError: 'tuple' object is not callable
