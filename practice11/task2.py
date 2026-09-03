# Завдання 2 | Тарасюк Н. | I-23

y = "2008"

def print_age(year):
    print(f"Year: {year}")

def get_age(year, current_year=2026):
    year = int(year)

    if year > current_year or year < 0:
        return -1
        print("After returnb")

    return current_year - year

print(print_age(y))
print(get_age(y))
 
age = get_age(y)

print("Кількість місяців:", age * 12)
print("Кількість тижнів:", age * 52)
print("Вік у 2030:", get_age(y, 2030))
print("Кількість місяців:", print_age(y)*12)