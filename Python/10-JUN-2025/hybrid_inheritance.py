class University:
    def __init__(self):
        self.university_name="Andhra University"
    def display(self):
        print(f"{self.university_name}")
class Course(University):
    def __init__(self,course):
        University.__init__(self)
        self.course_name=course
    def display(self):
        print(f"{self.university_name} having {self.course_name} course")
class Branch(University):
    def __init__(self,branch):
        University.__init__(self)
        self.branch_name=branch
    def display(self):
        print(f"{self.university_name} having {self.branch_name} branch")
class Student(Course,Branch):
    def __init__(self,course,branch,name):
        Course.__init__(self,course)
        Branch.__init__(self,branch)
        self.student_name=name
    def display(self):
        print(f"I am {self.student_name} pursuing {self.branch_name} it having {self.course_name} course in {self.university_name}")
class Faculty(Branch):
    def __init__(self,branch,faculty):
        Branch.__init__(self,branch)
        self.faculty_name=faculty
    def display(self):
        print(f"Im {self.faculty_name} teaching for {self.branch_name} branch")
student_1=Student("python","BCA","Sai")
print(student_1.student_name)
student_1.display()
faculty_1=Faculty("BCA","Teja")
faculty_1.display()