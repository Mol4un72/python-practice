schedule = {
    "Mon": ["Programming", "Math", "English"],
    "Tue": ["Physics", "Programming", "Ukrainian"],
    "Wed": ["Math", "English", "History"],
    "Thu": ["Programming", "Physics", "Math"],
    "Fri": ["English", "Ukrainian", "Programming"]
}

for day, subjects in schedule.items():
    print(f"{day}: {len(subjects)} - {', '.join(subjects)}")

total = sum(len(subjects) for subjects in schedule.values())
print(total)

max_day = max(schedule, key=lambda d: len(schedule[d]))
print(max_day)

all_subjects = set()
for subjects in schedule.values():
    all_subjects.update(subjects)
print(all_subjects, len(all_subjects))

mon_set = set(schedule["Mon"])
wed_set = set(schedule["Wed"])
print(mon_set & wed_set)
print(mon_set - wed_set)

def subject_counts(schedule_dict):
    counts = {}
    for subjects in schedule_dict.values():
        for s in subjects:
            counts[s] = counts.get(s, 0) + 1
    return counts

counts = subject_counts(schedule)
sorted_subjects = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for i, (subject, count) in enumerate(sorted_subjects, 1):
    print(f"{i}. {subject} - {count}")