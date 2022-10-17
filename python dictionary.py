person = {'name': 'Aouwal', 'age': 32, 'isMale': True}
# Access elements
name = person.get('name')
age = person['age']
# print(age)

# Access all keys/values

key_list = list(person.keys())
value_list = list(person.values())
# print(value_list)

#  Change the Value
person['age'] = 33
person.update({'age':33})

# print(person)

# New Key and Value 
person['profession'] = 'Seo Specialist'


# Remove Dictionary Element
person.pop('age')
print(person)