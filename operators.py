Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> ##in operator
>>> L1=["apple","orange","guava","grapes"]
>>> print("apple" in L1)
True
>>> print("cherry" in L1)
False
>>> print("guava" not in L1)
False
>>> print("cherry" not in L1)
True
>>> 
>>> ##Bitwise operator
>>> a=10
>>> b=5
>>> print(a & b)
0
>>> print(a | b)
15
>>> print(a ~ b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(~a)
-11
>>> print(~b)
-6
>>> print( a ^ b)
15
>>> print(a >> b)
0
>>> print(a << b)
320
>>> ## identity operator
>>> l1=10
>>> l2=10
>>> print(id(l1))
140707178890440
>>> print(id(l2))
140707178890440
>>> print(l1 is l2)
True
>>> print(l1 is not l2)
False
>>> print(l1 is l2)
True
