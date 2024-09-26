class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        self.students[student_id] = Student(student_id, name)

    def add_course(self):
        code = input("Enter course code: ")
        title = input("Enter course title: ")
        self.courses[code] = Course(code, title)

    def enroll_student_in_course(self):
        student_id = input("Enter student ID: ")
        course_code = input("Enter course code: ")
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course:
            student.enroll(course)
        else:
            print("Student or course not found.")

    def print_student_info(self):
        student_id = input("Enter student ID to view info: ")
        student = self.students.get(student_id)
        if student:
            print(f"Student ID: {student.student_id}, Name: {student.name}")
            for course in student.courses.values():
                grade = course.get_grade(student)
                print(f"  Enrolled in: {course.title}, Grade: {grade if grade is not None else 'Not graded'}")
            print(f"GPA: {student.get_gpa():.2f}")
        else:
            print("Student not found.")


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll(self, course):
        self.courses[course.code] = course
        course.add_student(self)

    def add_grade(self, course_code, grade):
        if course_code in self.courses:
            self.courses[course_code].add_grade(self, grade)
        else:
            print(f"Student not enrolled in course: {course_code}")

    def get_gpa(self):
        total_points = 0
        total_courses = 0
        for course in self.courses.values():
            grade = course.get_grade(self)
            if grade is not None:
                total_points += grade
                total_courses += 1
        return total_points / total_courses if total_courses > 0 else 0


class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title
        self.enrolled_students = {}
        self.grades = {}

    def add_student(self, student):
        self.enrolled_students[student.student_id] = student

    def add_grade(self, student, grade):
        self.grades[student.student_id] = grade

    def get_grade(self, student):
        return self.grades.get(student.student_id, None)


def main():
    system = StudentManagementSystem()

    while True:
        choice = input("\n1. Add Student\n2. Add Course\n3. Enroll Student\n4. View Student Info\n5. Exit\nChoose an option: ")
        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.add_course()
        elif choice == "3":
            system.enroll_student_in_course()
        elif choice == "4":
            system.print_student_info()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
