# Завдання 3 | Тарасюк Н. | I-23

name = 'Nazar'
surname = 'Tarasiuk'

def get_initials(name: str, surname: str) -> str:
    print(f"Initials: {name[0].upper()}.{surname[0].upper()}.")

def count_letters(text: str, letter: str = "a") -> int:
    """Count the occurrences of a specific letter in the text."""
    count = 0

    for char in text:
        if char.lower() == letter.lower():
            count += 1

    return count

def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count

def reverse_text(text: str) -> str:
    result = ""

    for char in text:
        result = char + result

    return result

print(f"{name} {surname}")
print("Initials:", get_initials(name, surname))

c = len(surname)
vowels = count_vowels(surname)
consonants = c - vowels

print("Vowels:", vowels)
print("Consonants:", consonants)

for vowel in "aeiou":
    print(f"{vowel}:", count_letters(surname, letter=vowel))

print("Reversed surname:", reverse_text(surname))

print("Docstring:", count_letters.__doc__)
print("Annotations:", count_letters.__annotations__)
