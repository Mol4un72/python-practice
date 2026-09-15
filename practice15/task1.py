c = len("Tarasiuk")
grades = [10, 7, 9, 11, 8, 6, 5, 4]

print(grades)
print(len(grades))
print(sum(grades))
print(max(grades))
print(min(grades))
print(f"{sum(grades)/len(grades):.2f}")

print(sorted(grades, reverse=True))
print(grades)

print(sorted(grades, reverse=True)[:3])
print(sorted(grades)[:3])

worst_index = grades.index(min(grades)) + 1
print(worst_index)

above_avg = [g for g in grades if g > sum(grades)/len(grades)]
print(above_avg)
print(len(above_avg))

print(12 in grades)
print(1 in grades)

grades.append(c % 12 + 1)
print(grades)

grades.insert(0, 12)
print(grades)

min_val = min(grades)
grades.remove(min_val)
print(grades)

last = grades.pop()
print(f"Removed last grade: {last}")
print(grades)

print(grades.count(12))

grades.sort()
print(grades)