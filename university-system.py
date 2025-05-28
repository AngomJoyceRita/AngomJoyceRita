
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Student is a type of Person
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print("Student ID:", self.student_id)
        print("Course:", self.course)


# Lecturer is a type of Person
class Lecturer(Person):
    def __init__(self, name, age, lecturer_id, department):
        super().__init__(name, age)
        self.lecturer_id = lecturer_id
        self.department = department

    def display_info(self):
        super().display_info()
        print("Lecturer ID:", self.lecturer_id)
        print("Department:", self.department)


# Staff is a type of Person
class Staff(Person):
    def __init__(self, name, age, staff_id, role):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.role = role

    def display_info(self):
        super().display_info()
        print("Staff ID:", self.staff_id)
        print("Role:", self.role)


# Create one object of each type
student = Student("Alice", 20, "U/20/98231", "Computer Science")
lecturer = Lecturer("Dr. Abasa", 45, "L/9723/U", "Software Engineering")
staff = Staff("Mrs. Joan", 35, "S/0238/T", "Secretary")

# Show their info
print("Student Info:")
student.display_info()

print("\nLecturer Info:")
lecturer.display_info()

print("\nStaff Info:")
staff.display_info()
