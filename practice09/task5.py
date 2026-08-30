# Завдання 5 | Тарасюк Н. | I-23

d = 14
c = 8
count = 0
i = 1
sum = 0
prime_count = 0

n = d * c

while n >= i:
    if n % i == 0:
        sum += i
        count += 1
    i += 1

while i < n:
    if n % i == 0:
        print("Not a prime number")
        break
    i += 1
else:
    print("Prime number")

number = 2

while number <= n:
    i = 2

    while i < number:
        if number % i == 0:
            break
        i += 1
    else:
        print(f"Prime numbers: {number}")
        prime_count += 1

    number += 1

print(f"Sum: {sum}")
print(f"Count: {count}")
print(f"Number of prime numbers: {prime_count}")