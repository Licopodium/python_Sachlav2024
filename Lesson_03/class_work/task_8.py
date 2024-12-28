grades = list(map(int, input("Enter grades for five exams: ").split()))

if all(1 <= grade <= 100 for grade in grades) and len(grades) == 5:
    print(max(grades))
else:
    print("Error: All grades must be integers between 1 and 100, and exactly 5 grades must be provided.")


