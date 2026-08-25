# Завдання 4 | Тарасюк Н. | I-23

grade = int(input("Enter yout grade:"))
lessons = int(input("Enter your attendance:"))
status = None

if grade < 0 or grade > 100:
    print("Enter valid grade!")
    exit()

if grade >= 90:
    print("Your grade is: A")
    gradeLetter = "A"
    status = "passed"
elif grade >= 82:
    print("Your grade is: B")
    gradeLetter = "B"
    status = "passed"
elif grade >= 74:
    print("Your grade is: C")
    gradeLetter = "C"
    status = "passed"
elif grade >= 64:
    print("Your grade is: D")
    status = "passed"
    gradeLetter = "D"
elif grade >= 60:
    print("Your grade is: E")
    gradeLetter = "E"
    status = 'passed'
else:
    print("Your grade is: F")
    gradeLetter = "F"
    status = "failed"

if lessons > 16 * 0.3:
    print("Denial of admission to the exam!")
    status = 'failed'


print(f"Your grade is: {gradeLetter} ({grade}), {status} ")