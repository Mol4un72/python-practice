about = "I study Python at college and I like playing chess"

words = about.split()

print(len(words))
print(max(words, key=len))
print(words[::-1])

print(about.lower().count("a"))

print(about.title())

print(about.replace(" ", "_"))


def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


print(is_palindrome("Tarasiuk Nazar Andriyovich"))
print(is_palindrome("Never odd or even"))


name = "Nazar"

day = 3

encrypted = ""

for letter in name.lower():
    encrypted += chr((ord(letter) - ord("a") + day) % 26 + ord("a"))

print(encrypted)

decrypted = ""

for letter in encrypted:
    decrypted += chr((ord(letter) - ord("a") - day) % 26 + ord("a"))

print(decrypted)