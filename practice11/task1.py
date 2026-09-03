# Завдання 1 | Тарасюк Н. | I-23

name = 'Nazar'
surname = 'Tarasiuk'
group = 'I-23'
y = '2026'

def print_card():
    print(f'Name: {name}')
    print(f'Surname: {surname}')
    print(f'Group: {group}')
    print(f'Year: {y}')
print_card()

def print_card_args(name, surname, y, group="I-23"):
    print(f'Name: {name}')
    print(f'Surname: {surname}')
    print(f'Group: {group}')
    print(f'Year: {y}')
print_card_args(name, surname, y, group)
print_card_args(name=name, surname=surname, y=y, group=group)
print_card_args(name, surname, y=y, group=group)

print_card_args("Ivan")
print_card_args(name="Ivan", "Petrenko")