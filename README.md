# Python Basics

## Python Print Function
```python
print('Md Abdul Aouwal')
# If you want to use separators 
print('Abdul','Aouwal', sep="***")
# newline = \n
# i'm = i\'m
# tab or 4 space = \t
```

## Python Variable 
1. variable store data 
2. Must start with character or underscore  (name, _name )
3. Can't start with number
4. A-z, 0-9, _ allowed
5. age , Age, AGE all are different 

## Python data types

1. Text types --> String
2. Number --> integer(5,6,7), float(5.0, 6.3), complex (2+3j)
3. Boolean -- True, False 
4. Sequence --> List, tuple , Range 
5. Mapping Type - Dictionary
6. Set 
7. None 

## Data Casting 
Convert one type to another type

1. int() --> Convert string or float to integer
2. str() --> Convert to String
3. float() --- > Convert to float 

## Python Operators 
1. Arthmetic Operators : +,-,*,/,%(Modulus Operators), **(Exponent), //(Floor Division)
2. Assignment Operators:  =, y+=3 ( y = y+3)
3. Comparison Operators:  == (equal), != (Not equal), > (Greater than), < (less than), >=(Greater than Equal), <= (Less than Equal)
4. Logical Operators: and , or , not
5. Identity Operators : is, is not
6. Membership Operators: is , not in

## python list
1. List is sequence of data, mulitple value or data can be stored
2. access: listname[indexnumber]
```python
fruits = ['Banana', 'Mango', 'Apple]
fruits[1]
```
3. List element can be changed
```python
fruits = ['Banana', 'Mango', 'Apple]
fruits[1]='Orange'
print(fruits)
# output: ['Banana', 'Orange', 'Apple]
```
4. Adding Element to the list: Listname.append(Data) - at the end of the list, list.insert(index, data) at index position
5. List element remove: list.pop()-- last element will removed, list.pop(2)-- index item 2 will be removed
6. remove by value: list.remove(data), list.clear -- empty list 

## Dictionary
1.  used to store data values in key:value pairs.
2. Access: 
```python
mobile = {'model':'I phone 16', 'price': 380000}
mobile['price'] # 380000
mobile.getitem('model')
```
3. Change or add
```python
mobile = {'model':'I phone 16', 'price': 380000}
mobile['price'] = 50000 
mobile.getitem({'model':'I phone 16'})
```
4. remove 
```python
mobile = {'model':'I phone 16', 'price': 380000}
mobile.pop('price')
```

5. Keys or values list 
```python
mobile = {'model':'I phone 16', 'price': 380000}
mobile.keys()
mobile.values()
```