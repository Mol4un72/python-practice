# Завдання 2 | Тарасюк Н. | I-23

birthday = int(input("Enter yout birthday (ddmmyyyy):"))
count = 0
sum = 0
biggest = 0
smallest = 0

if birthday <= 0:
    print("Enter positive number")
else:
    while birthday > 0:
        number = birthday % 10
        sum += number
        count += 1

        if number > biggest:
            biggest = number

        if number < smallest:
            smallest = number
            
        birthday = birthday // 10

print(f"Count: {count}")
print(f"Sum: {sum}")
print(f"Biggest: {biggest}")
print(f"Smallest {smallest}")