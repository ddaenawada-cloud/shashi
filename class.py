class students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


s = students("John", 20, 85)
s1 = students("Alice", 22, 90)
s2 = students("Bob", 19, 80)
s3 = students("Charlie", 21, 95)

for student in [s, s1, s2, s3]:
    student.display_info()
    if student.grade >= 90:
        print(f"{student.name} has secured a distinction.")
    else:
        print(f"{student.name} has a grade below the distinction level.")

total = s.grade + s1.grade + s2.grade + s3.grade
average = total / 4
print(f"The average grade of the students is: {average}")
print(f"The total grade of the students is: {total}")

total = sum(student.grade for student in [s, s1, s2, s3])
print(f"The total grade of the students is: {total}")
    