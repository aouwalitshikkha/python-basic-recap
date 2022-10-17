number = 2
while number > 1:
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    person = [age, name]
    number -= 1
    
print(person)