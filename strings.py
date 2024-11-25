# string ha hamon reshte haye addadian. 

type ('salam jadi')
# ve inja neshon mide ke stringe 
# to kheili az jahaye computer ma az 0 shoro mikonim be shomaresh kardan va na az 1.

#len rule:
# vaghti az in toye terminal python setafade mikonim kari ke anjam midim inke tol on ye chiz ro mikhaim.

len(a) # nahveye neveshte shodanesh 

# Slice Rule: 
# 2 halat mokhtalef vojod dare ke mitonim azash estefade bokonim: 
# 1. s = 'man daram miram'
# s[0] = m / s[2] = n 
# s[:3] = man => kari ke dar inja etefagh mi ofte ineke az aval mire ta sar 3 
# 2. s = 'man daram miram'
# s[3:] = space daram miram => khode 3 ro shamel mishe to enteha 
# 3. s = 'man daram miram'
# s[3:8] => yani az 3 shoro mishe ta sar 8 yani khode 8 ro shamel nemishe. 
# s = 'man daram miram'
# 4. s[-1] = m => az akhar avalie ro mide yani vaghti az akhar mirim shomarsh mishe -1 , -2 , -3 , ...
# s [: -3] => inja mitone daghighan in jori bashe ke az tah shoro mikone be khondan to sar -3 va khde -3 ro shmael nemishe
# pay attention : space ha ham shomaresh mishavand.
# baraye inke betonim taghirati ro barash anjam bedim be in sorat amal mikonim: 
# s = 'man daram miram'
# s = 'M' + s[1:]
# Man daram miram 
# Codes in Class 
>>> type ('salam jadi')
<class 'str'>
>>> a = 'salam'
>>> a
'salam'
>>> a[0]
's'
>>> a[4]
'm'
>>> a[5]
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    a[5]
    ~^^^
IndexError: string index out of range
>>> len(a)
5
>>> a = 'salam'
>>> tool = len(a)
>>> tool
5
>>> for i in range(0, tool):
...     print (i, a[i])
...
0 s
1 a
2 l
3 a
4 m
>>> a = 'salam kojaaee'
>>> for i in range(0, len(a)):
...     print(a[i])
...
s
a
l
a
m

k
o
j
a
a
e
e
>>> for letter in 'my string':
...     print (letter)
...
m
y

s
t
r
i
n
g
>>> string ='this is a sample string to count as'
>>> for harf in string:
...     print(harf)
...
t
h
i
s

i
s

a

s
a
m
p
l
e

s
t
r
i
n
g

t
o

c
o
u
n
t

a
s
>>> count = 0
>>> for letter in string:
...     if letter == 'a':
...         count = count + 1
...
>>> count
3
>>> len(string)
35
>>> s = 'man daram miram'
>>> s[0]
'm'
>>> s = 'man daram miram'
>>> s[3]
' '
>>> s[:3]
'man'
>>> s[3:]
' daram miram'
>>> s[1:]
'an daram miram'
>>> s
'man daram miram'
>>> s = 'M' + s[1:]
>>> s
'Man daram miram'