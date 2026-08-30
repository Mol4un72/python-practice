# Завдання 3 | Тарасюк Н. | I-23

name = "Nazar"
surname = "Tarasiuk"

vowels = 0
consonants = 0

for letter in name + surname:
    if letter.lower() in "aeiouy":
        vowels += 1
    else:
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Total:", vowels + consonants)
print("Length:", len(name + surname))