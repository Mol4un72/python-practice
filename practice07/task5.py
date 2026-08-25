# Завдання 5 | Тарасюк Н. | I-23

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

if month < 1 or month > 12:
    print("Date is invalid: month must be between 1 and 12")
elif year <= 0:
    print("Date is invalid: year must be positive")
else:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_days = 29
        else:
            max_days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30
    else:
        max_days = 31
    if day < 1:
        print("Date is invalid: day must be at least 1")
    elif day > max_days:
        print(f"Date is invalid: month {month} has only {max_days} days")
    else:
        print("Date is valid")