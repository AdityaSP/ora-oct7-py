Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
li = [1,2,3]
>>> li[0]
1
>>> d = { 'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> len(d)
2
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['name']
'Aditya'
>>> d['email']
'sp.aditya@gmail.com'
>>> d.keys()
dict_keys(['name', 'email'])
>>> d.values()
dict_values(['Aditya', 'sp.aditya@gmail.com'])
>>> d['city']
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d['city']
KeyError: 'city'
>>> d['city']='Bangalore'
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'Bangalore'}
>>> d['city']='New York'
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'New York'}
>>> d['phone']=['2341232344', '3445423423']
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'New York', 'phone': ['2341232344', '3445423423']}
>>> d['phone']
['2341232344', '3445423423']
>>> d['phone'][0]
'2341232344'
>>> d['phone'][1]
'3445423423'
>>> d['address']={ 'home': 'asdklj ieurlkjdf', 'work': 'woeiurnglkjodif' }
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'New York', 'phone': ['2341232344', '3445423423'], 'address': {'home': 'asdklj ieurlkjdf', 'work': 'woeiurnglkjodif'}}
>>> d['address']['work']
'woeiurnglkjodif'
>>> 
>>> 
>>> 

>>> t = (1,2,3)
>>> type(t)
<class 'tuple'>
>>> 
>>> 
>>> 
>>> # unpacking a tuple
>>> 
>>> t
(1, 2, 3)
>>> len(t)
3
>>> a,b,c = t
>>> a
1
>>> b
2
>>> c
3
>>> t = b,c
>>> t
(2, 3)
>>> b
2
>>> c
3
>>> temp = b
>>> b = c
>>> c = temp
>>> b
3
>>> c
2
>>> b, c = c, b
>>> b
2
>>> c
3
>>> d
{'name': 'Aditya', 'email': 'sp.aditya@gmail.com', 'city': 'New York', 'phone': ['2341232344', '3445423423'], 'address': {'home': 'asdklj ieurlkjdf', 'work': 'woeiurnglkjodif'}}
>>> for key in d.keys():
	print("key", key, "value", d[key])

	
key name value Aditya
key email value sp.aditya@gmail.com
key city value New York
key phone value ['2341232344', '3445423423']
key address value {'home': 'asdklj ieurlkjdf', 'work': 'woeiurnglkjodif'}
>>> d.items()
dict_items([('name', 'Aditya'), ('email', 'sp.aditya@gmail.com'), ('city', 'New York'), ('phone', ['2341232344', '3445423423']), ('address', {'home': 'asdklj ieurlkjdf', 'work': 'woeiurnglkjodif'})])
>>> for item in d.items():
	print(item)
	print(type(item))

	
('name', 'Aditya')
<class 'tuple'>
('email', 'sp.aditya@gmail.com')
<class 'tuple'>
('city', 'New York')
<class 'tuple'>
('phone', ['2341232344', '3445423423'])
<class 'tuple'>
('address', {'home': 'asdklj ieurlkjdf', 'work': 'woeiurnglkjodif'})
<class 'tuple'>
>>> for item in d.items():
	k,v = item
	print("key", k, "value", v)

	
key name value Aditya
key email value sp.aditya@gmail.com
key city value New York
key phone value ['2341232344', '3445423423']
key address value {'home': 'asdklj ieurlkjdf', 'work': 'woeiurnglkjodif'}
>>> for k,v in d.items():
	print("key", k, "value", v)

	
key name value Aditya
key email value sp.aditya@gmail.com
key city value New York
key phone value ['2341232344', '3445423423']
key address value {'home': 'asdklj ieurlkjdf', 'work': 'woeiurnglkjodif'}
>>> li = ['Windows', 'Android', 'Linux'']
      
SyntaxError: EOL while scanning string literal
>>> li = ['Windows', 'Android', 'Linux']
>>> for os in li:
	print(os)

	
Windows
Android
Linux
>>> for os in enumerate(li):
	print(os)

	
(0, 'Windows')
(1, 'Android')
(2, 'Linux')
>>> for idx, os in enumerate(li):
	print(os , 'at', idx)

	
Windows at 0
Android at 1
Linux at 2
>>> fn = ['Bill', 'Steve', 'Roger']
>>> ln = ['Gates', 'Jobs', 'Federer']
>>> for item in zip(fn, ln):
	print(item)

	
('Bill', 'Gates')
('Steve', 'Jobs')
('Roger', 'Federer')
>>> for f,l in zip(fn, ln):
	print(f, l)

	
Bill Gates
Steve Jobs
Roger Federer
>>> 
