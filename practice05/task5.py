# Завдання 5 | Тарасюк Н. | I-23

day = 1
month = 2

is_positive = day > 0
is_even = day % 2 == 0
both_conditions = is_positive and is_even

print(f"Positive: {is_positive}, Type: {type(is_positive)}")
print(f"Even: {is_even}, Type: {type(is_even)}")
print(f"Positive and Even: {both_conditions}, Type: {type(both_conditions)}")

num = day * month

is_positive_2 = num > 0
is_even_2 = num % 2 == 0
both_conditions_2 = is_positive_2 and is_even_2

print(f"Positive: {is_positive_2}, Type: {type(is_positive_2)}")
print(f"Even: {is_even_2}, Type: {type(is_even_2)}")
print(f"Positive and Even: {both_conditions_2}, Type: {type(both_conditions_2)}")