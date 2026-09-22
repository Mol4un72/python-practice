full_name = " tARASIUK   nazar andriyovich  "

full_name = " ".join(full_name.split()).title()

print(full_name)
print(len(full_name))

surname, name, patronymic = full_name.split()

print(surname[0])
print(surname[-1])

print(surname[::-1])

print(f"{surname} {name[0]}. {patronymic[0]}.")

print(surname[0] + name[0] + patronymic[0])

vowels = "aeiou"
count = 0

for letter in full_name.lower():
    if letter in vowels:
        count += 1

print(count)

group = "I-23"

dash = group.find("-")

print(group[:dash])
print(group[dash + 1:])

print(group[dash + 1:].isdigit())

login = name[0].lower() + "." + surname.lower()
email = login + "@student.edu.ua"

print(login)
print(email)