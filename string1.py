# baraye moghayese string ha kari ke anjam midim inke tartib ro raayat mikonim: 
# tartib ha : 
# oni ke payeen tare > oni ke balatare => to tartib dictionari yani masal b az a bozotare chon b bad az a hast 
# 2. horof kochik arjahiet daran az horof bozorg a > A
# ma dar python ye chizi darim be esm method va hamechi class hast 
# class ha ye chiz hayee daran beesm method ke kheili nazdike be hamon funcition ha 
# mitonim az in method ha injori estefade bokonim: ------+.+------+() => 'jadi'.upper() => result : 'JADI'
# baraye inke motevajeh beshim ke baraye ye class che method hayee ro darim az in ravesh stefadeh mikonim :
# dir ('jadi')
# baraye inke bekhaim ye motagheir hayee ke khodemon tarif kardim ro be ye reshte string ezafe bokoinm be in sorat amal mikonim : 
# as %s in '' estefade mikonim va as % kharej ''
#print ('hello %s chetori? midooni % salet shode?' % (name , sen))
# result : hello jadi chetori? midooni 40 salet shode?
# %s => yani string hata agar varaiable haye ma integer & float & ... bashe be string tabdil mikone
# %i => tabdil be integer shodan 
>>> 'a' in  'jadi'
True
>>> 'ad' in 'jadi'
True
>>> 'add' in 'jadi'
False
>>> name = 'jadi'
>>> name == 'jadi'
True
>>> name
'jadi'
>>> family = 'farzaneh'
>>> name == family
False
>>> name
'jadi'
>>> family
'farzaneh'
>>> name > family
True
>>> 'a' > 'b'
False
>>> 'bia berim' > 'added aval'
True
>>> 'A' >'a'
False
>>> 'a' > 'A'
True
>>> type ('hello')
<class 'str'>
>>> 'jadi'.upper()
'JADI'
>>> dir('jadi')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.count)
Help on method_descriptor:

count(self, sub[, start[, end]], /) unbound builtins.str method
    Return the number of non-overlapping occurrences of substring sub in string S[start:end].

    Optional arguments start and end are interpreted as in slice notation.

>>> 'salam jadi'.count('a')
3
>>> s = 'hello'
>>> type(s)
<class 'str'>
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s.upper()
'HELLO'
>>> s.lower()
'hello'
>>> s.find('l')
2
>>> s.find('l', 3)
3
>>>
>>> 'hjkahsdkjhkshakhkjsfh '.strip()
'hjkahsdkjhkshakhkjsfh'
>>> 'hello .startswith('h')
  File "<python-input-29>", line 1
    'hello .startswith('h')
                         ^
SyntaxError: unterminated string literal (detected at line 1)
>>> 'hello'.startswith('h')
True
>>> 'Hello'.startswith('h')
False
>>> 'Hello'.lower().startswith('h')
True
>>> print('hello')
hello
>>> name = 'jadi'
>>> print('hello' , name )
hello jadi
>>> print ('hello %s' % name)
hello jadi
>>> print ('hello %s chetori?' % name)
hello jadi chetori?
>>> sen = 40
>>> print ('hello %s chetori? midooni % salet shode?' % (name , sen))
hello jadi chetori? midooni 40alet shode?
>>> print ('hello %s chetori? midooni %s salet shode?' % (name , sen))
hello jadi chetori? midooni 40 salet shode?
>>>






















