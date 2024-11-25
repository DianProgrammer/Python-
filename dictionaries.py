string = 'salam.jadi is here and tesdting python for run'

counter = dict()

for letter in string: 
    print (letter)

    if letter in counter: 
        counter[letter] += 1
    else:
        counter[letter] = 1

    print(counter)

string = 'salam.jadi is here and tesdting python for run'

counter = dict()

for letter in string: 
    print (letter)

    if letter in counter: 
        counter[letter] += 1
    else:
        counter[letter] = 1
    for this_one in list(counter.keys()):
        print('%s appeared %s times' % (this_one, counter[this_one]))


string = 'salam.jadi is here and tesdting python for run'

counter = dict()

for letter in string: 
    
        counter[letter]  = counter.get(letter, 0) + 1

for this_one in list(counter.keys()):
        print('%s appeared %s times' % (this_one, counter[this_one]))




>>> a = dict()
>>> f2t = dict()
>>> f2t['yek'] = 'bir'
>>> f2t['do'] = 'ikki'
>>> f2t
{'yek': 'bir', 'do': 'ikki'}
>>> ghad = {}
>>> type(ghad)
<class 'dict'>
>>> ghad = {'jadi':180, hasan': 200, 'zahra':167}
  File "<python-input-7>", line 1
    ghad = {'jadi':180, hasan': 200, 'zahra':167}
                                           ^
SyntaxError: unterminated string literal (detected at line 1)
>>> ghad = {'jadi':180, 'hasan': 200, 'zahra':167}
>>> ghad
{'jadi': 180, 'hasan': 200, 'zahra': 167}
>>> ghad['jadi']
180
>>> f2t['yek']
'bir'
>>> len(f2t)
2
>>> ghad.keys()
dict_keys(['jadi', 'hasan', 'zahra'])
>>> ghad
{'jadi': 180, 'hasan': 200, 'zahra': 167}
>>> ghad.values()
dict_values([180, 200, 167])
>>> lsit(ghad.keys())
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>
    lsit(ghad.keys())
    ^^^^
NameError: name 'lsit' is not defined
>>> list(ghad.keys())
['jadi', 'hasan', 'zahra']
>>> list(ghad.values())
[180, 200, 167]
>>> 'jadi' in ghad
True
>>> ghad
{'jadi': 180, 'hasan': 200, 'zahra': 167}
>>> 180 in ghad
False
>>> ghad['farzaneh']
Traceback (most recent call last):
  File "<python-input-22>", line 1, in <module>
    ghad['farzaneh']
    ~~~~^^^^^^^^^^^^
KeyError: 'farzaneh'
>>> ghad.get('jadi')
180
>>> ghad.get('jadi1234')
>>> ghad.get('farzaneh', 1)
1
        