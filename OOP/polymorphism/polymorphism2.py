class Student:
    def __init__(self, name, student_id, email):
        self.name = name
        self.student_id = student_id
        self.email = email
        self.courses = []  # Common feature for all students
    
    def enroll(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name} has enrolled in {course_name}.")
    
    def drop_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"{self.name} has dropped {course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")
    
    def display_info(self):
        print(f"Student Name: {self.name}\nStudent ID: {self.student_id}\nEmail: {self.email}\nCourses Enrolled: {', '.join(self.courses) if self.courses else 'None'}\n")
    
    def get_student_type(self):
        return "General Student"


class RegularStudent(Student):
    def __init__(self, name, student_id, email, credits):
        super().__init__(name, student_id, email)
        self.credits = credits  # Unique attribute for regular students
    
    def display_info(self):
        super().display_info()
        print(f"Course Load: {self.credits} credits\n")
    
    def get_student_type(self):
        return "Regular (Full-Time) Student"


class PartTimeStudent(Student):
    def __init__(self, name, student_id, email, work_hours):
        super().__init__(name, student_id, email)
        self.work_hours = work_hours  # Unique attribute for part-time students
    
    def display_info(self):
        super().display_info()
        print(f"Working Hours: {self.work_hours} hours/week\n")
    
    def get_student_type(self):
        return "Part-Time Student"


# Example Usage
student1 = RegularStudent("Ashok Kumar Yadav", 1001, "ashok@gmail.com", 18)
student2 = PartTimeStudent("Niraj Prasad Karna", 1002, "niraj@gmail.com", 20)

# Enroll students in courses
student1.enroll("BSC CSIT",)
student2.enroll("Computer Science")

# Function demonstrating polymorphism
def print_student_details(student):
    print("--- Student Details ---")
    student.display_info()
    print(f"Student Type: {student.get_student_type()}\n")

# Using polymorphism
students = [student1, student2]
for student in students:
    print_student_details(student)

# Drop a course
student1.drop_course("Mathematics")
student1.display_info()

