
# tuple kheili shabih list ha hastand vali immutable hastand yani agar yabr dorosteshon kardim dige nemitonim taghiresh bedim.
# tuple = (1, 2, 3) / list = [1, 2, 3]
>>> t = (1, 2, 3)
>>> t
(1, 2, 3)
>>> type(t)
<class 'tuple'>
>>> t[0]
1
>>> t[0] = 45
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    t[0] = 45
    ~^^^
TypeError: 'tuple' object does not support item assignment
>>> (4)
4
>>> (4,)
(4,)
>>> type((4,))
<class 'tuple'>
>>> t = tuple()
>>> t = (0, 1, 2, 3, 4, 'hello')
>>> t[1:3]
(1, 2)
>>> a = [1, 2]
>>> x, y = a
>>> x
1
>>> y
2
>>> x, y = 4, 5
>>> x
4
>>> x, y =4, 5, 6
Traceback (most recent call last):
  File "<python-input-17>", line 1, in <module>
    x, y =4, 5, 6
    ^^^^
ValueError: too many values to unpack (expected 2)
>>> a = 1
>>> b = 2
>>> a, b = b, a
>>> a
2
>>> b
1
>>> email = 'jadijadi@gmail.com'
>>> email.split('@')
['jadijadi', 'gmail.com']
>>> name, domian = email.split('@')
>>> name
'jadijadi'
>>> domain
Traceback (most recent call last):
  File "<python-input-27>", line 1, in <module>
    domain
NameError: name 'domain' is not defined. Did you mean: 'domian'?
>>> domian
'gmail.com'
>>> vazn = {'jadi' : 75 , 'sara' : 68 , 'jafar' : 80, 'mehdi' : 100}
>>> vazn
{'jadi': 75, 'sara': 68, 'jafar': 80, 'mehdi': 100}
>>> vazn.items()
dict_items([('jadi', 75), ('sara', 68), ('jafar', 80), ('mehdi', 100)])
>>> list(vazn.items())
[('jadi', 75), ('sara', 68), ('jafar', 80), ('mehdi', 100)]
>>> for name , vazn in list(vazn.items()):
...     print('vazn %s taghriban hast %s' % (name, vazn))
...
vazn jadi taghriban hast 75
vazn sara taghriban hast 68
vazn jafar taghriban hast 80
vazn mehdi taghriban hast 100
>>> phone = dict()
>>> phone['jadi'] = '0912'
>>> phone
{'jadi': '0912'}
>>> phone ['jadi', 'home'] = '0912'
>>> phone
{'jadi': '0912', ('jadi', 'home'): '0912'}