surname = "Tarasiuk"
letters = [ch for ch in surname.lower()]
c = len(letters)

print(letters)
print(c)

print(letters[0])
print(letters[len(letters)//2])
print(letters[-1])
print(letters[len(letters)-1])

print(''.join(letters[:3]))

print(''.join(letters[3:]))

second_letters = letters[1::2]
print(second_letters)

print(''.join(reversed(letters)))

print(''.join(letters[-2:]))

unique = []
for ch in letters:
    if ch not in unique:
        unique.append(ch)
print(unique)

cnt = {}
for ch in letters:
    cnt[ch] = cnt.get(ch, 0) + 1
repeated = [(ch, cnt[ch]) for ch in cnt if cnt[ch] > 1]
if repeated:
    for ch, n in repeated:
        print(f"{ch} {n}")
else:
    print("No repeated letters")

print(sorted(letters))