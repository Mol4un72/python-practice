def print_table(subjects):
    print("#  Subject        Pairs  Grade")
    for i, (title, pairs, grade) in enumerate(subjects, start=1):
        print(f"{i}  {title:<12} {pairs:<5} {grade}")

def main():
    print("Nazar Tarasiuk, I-23")
    subjects = [('Programming', 3, 11), ('Math', 2, 8), ('English', 2, 10), ('Physics', 1, 6), ('History', 2, 7)]
    print_table(subjects)
    total_pairs = sum(p for _, p, _ in subjects)
    print(f"Pairs per week: {total_pairs}")
    most_pairs = max(subjects, key=lambda x: x[1])
    print(f"Most pairs: {most_pairs[0]} ({most_pairs[1]})")
    weakest = min(subjects, key=lambda x: x[2])
    print(f"Weakest subject: {weakest[0]} ({weakest[2]})")
    titles = [s[0] for s in subjects]
    print(f"Titles: {titles}")
    grades = [s[2] for s in subjects]
    avg = sum(grades) / len(grades)
    print(f"Grades: {grades}, average: {avg:.2f}")
    high = [s[0] for s in subjects if s[2] >= 10]
    print(f"Grade 10+: {high}")
    for title, pairs, grade in subjects:
        print(f"{title}: {'#' * grade}")
    min_grade = min(g for _,_,g in subjects)
    for i, (title, pairs, grade) in enumerate(subjects):
        if grade == min_grade:
            new_grade = min(grade + 2, 12)
            subjects[i] = (title, pairs, new_grade)
            print(f"Retake: {title} {grade} -> {new_grade}")
            break
    print(f"Subjects: {subjects}")

if __name__ == '__main__':
    main()