# Завдання 1 | Тарасюк Н. | I-23

name = input('Enter your name: ')
age = int(input('Enter your age: '))
if not name:
    print('You did not enter your name.')
    name = 'Anonymous'
if not age:
    print('You did not enter your age.')
elif age < 0:
    print('Age cannot be negative.')
elif age <= 6:
    print(f'Hello, {name}! You are a child.')
elif age >= 7 and age <= 17:
    print(f'Hello, {name}! You are a schoolchild.')
elif age >= 18 and age <= 64:
    print(f'Hello, {name}! You are an adult.')
else: 
    print(f'Hello, {name}! You are a senior citizen.')
