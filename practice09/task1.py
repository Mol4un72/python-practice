# Завдання 1 | Тарасюк Н. | I-23

d = 2
c = 5
count = 0
total = 0
product = 1
odd = 0
even = 0

for i in range(d, 31): 
    print(i)
    i += d + 1
    count += 1
    total += i
    product *= i
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

average = (count + total + product) / 3

print(f"Count: {count}")
print(f"Total sum: {total}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Odd count: {odd}")
print(f"Even count: {even}")

# while cersion
print()

count_w = 0
total_w = 0
product_w = 1
even_w = 0
odd_w = 0

i = d

while i <= 31:
    i += 1
    count_w += 1
    total_w += i
    product_w *= i

    if i % 2 == 0:
        even_w += 1
    else:
        odd_w += 1

average_w = (count + total + product) / 3

print(f"Count_w: {count_w}")
print(f"Total sum_w: {total_w}")
print(f"Product_w: {product_w}")
print(f"Average_w: {average_w:.2f}")
print(f"Odd count_w: {odd_w}")
print(f"Even count_w: {even_w}")

print()
for i in range(c, 0, -1):
    print(i)
print()