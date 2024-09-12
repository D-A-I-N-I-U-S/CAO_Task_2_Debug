class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.grades = {}  # Dictionary to store grades for courses
        self.enrolled_courses = []  # List to store courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def performance_report(self):
        enrolled_course_names = [course.name for course in self.enrolled_courses]  # Get course names
        grades_report = {course: grade for course, grade in self.grades.items()}  # Course names and grades
        print(f"Student: {self.name}, Enrolled Courses: {', '.join(enrolled_course_names)}, Grades: {grades_report}")
        # Print student name, enrolled courses, and grades ------ SECOND PRINT PART

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course.name] = grade


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    def list_courses(self):
        return [course.name for course in self.courses]


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        self.lessons = []
        teacher.courses.append(self)  # Add this course to the teacher's course list

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            attendance_record = self.attendance.get(student, [])
            attendance_status = ", ".join([f"{date}, Attendance: {status}" for date, status in attendance_record])
            print(f"Student: {student.name}, Date: {attendance_status}")
            # Print student attendance - FIRST PRINT PART

    def add_lesson(self, *lessons):  # "variable-length argument" or "unpacking operator"
        self.lessons.extend(lessons)

    def get_lessons(self):
        if not self.lessons:
            print("No lessons added yet.")
        else:
            for lesson in self.lessons:
                print(f"Lesson: {lesson.name}, Date: {lesson.date}, Description: {lesson.description}")


class Lesson:
    def __init__(self, name, date, description, course):
        self.name = name
        self.date = date
        self.description = description
        self.course = course
        self.attendance = {}
        self.grades = {}

    def record_attendance(self, student, date, status):
        if student in self.course.students:
            self.attendance[student] = (date, status)

    def record_grade(self, student, grade):
        if student in self.course.students:
            self.grades[student] = grade

    def generate_report(self):
        for student, attendance in self.attendance.items():
            grade = self.grades.get(student, "N/A")
            print(f"Student: {student.name}, Attendance: {attendance[0]}: {attendance[1]}, Grade: {grade}")
            # Print student attendance and grade - SECOND PART

    def __str__(self):
        return self.name


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report()  # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report()  # Student: Alice, Course: Mathematics, Grade: A
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']

# Lessons example usage:

lesson1 = Lesson("Algebra Basics", "2024-02-01", "Algebra Textbook Chapter 1", math_course)
lesson2 = Lesson("Introduction to Geometry", "2024-02-08", "Geometry Workbook", math_course)

math_course.add_lesson(lesson1, lesson2)

math_course.get_lessons()
