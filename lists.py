>>> l = [4, 5, 9, -1, 1.5, 'jadi']
>>> l[0]
4
>>> l[:4]
[4, 5, 9, -1]
>>> l[-2]
1.5
>>> l2 = [l, 5, [1, 2]
... l2
...
  File "<python-input-4>", line 1
    l2 = [l, 5, [1, 2]
         ^
SyntaxError: '[' was never closed
>>> l2 = [l, 5, [1, 2]]
>>> l2
[[4, 5, 9, -1, 1.5, 'jadi'], 5, [1, 2]]
>>> len(12)
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    len(12)
    ~~~^^^^
TypeError: object of type 'int' has no len()
>>> len(l2)
3
>>> l2[0]
[4, 5, 9, -1, 1.5, 'jadi']
>>> for i in range(0, len(l2)):
...     print l2[i]
...
  File "<python-input-10>", line 2
    print l2[i]
    ^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> for i in range(0, len(l2)):
...     ...     print (l2[i])
...
  File "<python-input-11>", line 2
    ...     print (l2[i])
            ^^^^^
SyntaxError: invalid syntax
>>> for i in range(0, len(l2)):
...     print (l2[i])
...
[4, 5, 9, -1, 1.5, 'jadi']
5
[1, 2]
>>> l
[4, 5, 9, -1, 1.5, 'jadi']
>>> l[0]=8
>>> l
[8, 5, 9, -1, 1.5, 'jadi']
>>> for i in range(0, len(l)):
...     print (i, l[i])
...
0 8
1 5
2 9
3 -1
4 1.5
5 jadi
>>> for item in l:
...     print (item)
...
8
5
9
-1
1.5
jadi
>>> l
[8, 5, 9, -1, 1.5, 'jadi']
>>> l1 = [1, 2]
>>> l2 = ['jadi', 'mohsen']
>>> l1
[1, 2]
>>> l2
['jadi', 'mohsen']
>>> l1 + l2
[1, 2, 'jadi', 'mohsen']
>>> l2 * 3
['jadi', 'mohsen', 'jadi', 'mohsen', 'jadi', 'mohsen']
>>> type(l1)
<class 'list'>
>>> dir(l1)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> l1
[1, 2]
>>> l1.append('new')
>>> l1
[1, 2, 'new']
>>> l1.extend([5, 6, 7])
>>> l1
[1, 2, 'new', 5, 6, 7]
>>> l1
[1, 2, 'new', 5, 6, 7]
>>> del l1[2]
>>> l1
[1, 2, 5, 6, 7]
>>> l1.sort()
>>> l1
[1, 2, 5, 6, 7]
>>> l1.append(2)
>>> l1
[1, 2, 5, 6, 7, 2]
>>> l1.sort()
>>> l1
[1, 2, 2, 5, 6, 7]
>>> l1
[1, 2, 2, 5, 6, 7]
>>> l1.pop()
7
>>> l1
[1, 2, 2, 5, 6]
>>> l1
[1, 2, 2, 5, 6]
>>> next = l1.pop()
>>> next
6
>>> li
Traceback (most recent call last):
  File "<python-input-47>", line 1, in <module>
    li
NameError: name 'li' is not defined
>>> l1
[1, 2, 2, 5]
>>> l1.remove(2)
>>> l1
[1, 2, 5]
>>> l1.remove(2)
>>> l1
[1, 5]
>>> del l1[0]
>>> l
[8, 5, 9, -1, 1.5, 'jadi']
>>> l1.remove(5)
>>> l1
[]
>>> my list = ['a', 'b', 'c', 'd']
  File "<python-input-57>", line 1
    my list = ['a', 'b', 'c', 'd']
       ^^^^
SyntaxError: invalid syntax
>>> my_list = ['a', 'b', 'c', 'd']
>>> my_list.remove('b')
>>> my_list
['a', 'c', 'd']
>>> my_list
['a', 'c', 'd']
>>> len(my_list)
3
>>> max(my_list)
'd'
>>> min(my_list)
'a'
>>> my_list = [12 , 13, 19 , 8 , 20]
>>> sum(my_list)
72
>>> sum(my_list) / len(my_list)
14.4
>>> s = 'some words are here'
>>> type(s)
<class 'str'>
>>> s.split()
['some', 'words', 'are', 'here']
>>> s.split('a')
['some words ', 're here']
>>> s.split()
['some', 'words', 'are', 'here']
>>> list_of_words = s.split()
>>> list_of_words
['some', 'words', 'are', 'here']
>>> '-'.join()list_of_words)
  File "<python-input-75>", line 1
    '-'.join()list_of_words)
                           ^
SyntaxError: unmatched ')'
>>>  '-'.join()list_of_words
  File "<python-input-76>", line 1
    '-'.join()list_of_words
IndentationError: unexpected indent
>>> '-'.join(list_of_words)
'some-words-are-here'
>>> l2
['jadi', 'mohsen']
>>> 'bechasboone'.join(l2)
'jadibechasboonemohsen'
>>> a = 'salam'
>>> b = 'salam'
>>> a is b
True
>>> a = [1, 2, 3]
>>> type(a)
<class 'list'>
>>> b = [1, 2, 3]
>>> a == b
True
>>> a is b
False
>>> a = [1, 2, 3]
>>> b = a
>>> a is b
True
>>> a[0] = 'yoohoo'
>>> a
['yoohoo', 2, 3]
>>> b
['yoohoo', 2, 3]