# Завдання 4 | Тарасюк Н. | I-23

number = 0
count = 0
level = None

while True:
    number = int(input("Enter your mark: "))
    count += 1

    if number < 0:
        print("Number is negative")
    elif number > 100:
        print("Number is bigger than 100")
    else:
        if number >= 90:
            level = "A"
        elif number >= 82:
            level = "B"
        elif number >= 74:
            level = "C"
        elif number >= 64:
            level = "D"
        elif number >= 60:
            level = "E"
        else:
            level = "F"

        print(f"Your mark: {number} ({level})")
        print(f"Attempts: {count}")

        break



