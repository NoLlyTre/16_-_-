from models.student import Student

class StudentService:
    def get_demo_student(self):
        return Student(1, "вапва", "вапва", "авпвап@gmail.com")
