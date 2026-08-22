# Завдання 6 | Тарасюк Н. | I-23

name = input("Enter your name: ")
age = int(input("Enter your age: "))

in_range = 18 <= age <= 60
is_even = age % 2 == 0

both_conditions = in_range and is_even
one_condition = in_range or is_even

years_to_60 = 60 - age

print(f"Name: {name}")
print(f"Age in range 18-60: {in_range}")
print(f"Age is even: {is_even}")
print(f"Both conditions met: {both_conditions}")
print(f"At least one condition met: {one_condition}")
print(f"Years left to 60: {years_to_60}")