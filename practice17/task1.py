me = {
    "name": "Nazar",
    "surname": "Tarasiuk",
    "group": "I-23",
    "city": "Kyiv",
    "birth_year": 2008,
    "hobbies": ["chess", "running", "guitar"]
}

for key, value in me.items():
    print(f"{key}: {value}")

print(list(me.keys()))
print(len(me))

print(me.get("group"))
print(me.get("email", "unknown"))
# me["email"] would raise KeyError because "email" key doesn't exist in the dictionary yet

me["email"] = "nazar.tarasiuk@university.edu"
me["city"] = "Lviv"
removed = me.pop("birth_year")
print(removed)

print("phone" in me)

print(me)
