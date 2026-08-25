# Завдання 2 | Тарасюк Н. | I-23

num = int(input("Enter your number: "))
if num > 0:
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is positive")
elif num < 0:
    print("The number is negative")
elif num == 0:
    print("The number is equal to zero")