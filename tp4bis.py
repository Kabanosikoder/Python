from random import shuffle
# student grades list
grades = []
grades.append(85)
grades.append(90)
grades.append(78)
grades.append(92)
grades.append(88)

print("List of grades: ", grades)

grades.remove(78)
print("Removing grade 78")
print("List of grades: ", grades)

grades = sorted(grades)
print("Sorted list of grades: ", grades)

shuffle(grades)
print("Shuffled list of grades: ", grades)

print("Total number of grades: ", len(grades))

average_grades = sum(grades) / len(grades)
print("Average grade: ", average_grades)
