# Завдання 3 | Тарасюк Н. | I-23

num1 = int(input("Enter the first number:"))
action = str(input("Enter the action:"))
num2 = int(input("Enter the second number:"))

if action == "+":
    result = num1 + num2
elif action == "-":
    result = num1 - num2
elif action == "*":
    result = num1 * num2
elif action == "/":
    if num2 == 0:
        print("Error: division by zero is not allowed")
    else:
        result = num1 // num2
elif action == "//":
    if num2 == 0:
        print("Error: division by zero is not allowed")
    else:
        result = num1 // num2
elif action == "%":
    if num2 == 0:
        print("Error: division by zero is not allowed")
    else:
        result = num1 % num2
elif action == "**":
    result = num1 ** num2
else:
    print("Enter valid action")


print(f"{num1} {action} {num2} = {result}")