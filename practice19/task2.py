grades_text = "95, 88, 100, 73, 81"

grades = [int(x) for x in grades_text.split(", ")]

print(f"Середня: {sum(grades) / len(grades):.2f}")
print(f"Найвища: {max(grades)}")
print(f"Найнижча: {min(grades)}")

print(" | ".join(str(x) for x in grades))

subjects_text = "Python, Database, Mathematics, English, Programming"
subjects = subjects_text.split(", ")

print(f"{'№':<5}{'Предмет':<20}{'Оцінка':>8}")

for i in range(len(subjects)):
    print(f"{i + 1:<5}{subjects[i]:<20}{grades[i]:>8}")

longest = max(subjects, key=len)

print(longest)
print(len(longest))