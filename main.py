from services.student_service import StudentService
from views.console_view import ConsoleView

def main():
    view = ConsoleView()
    service = StudentService()

    view.show_welcome()
    student = service.get_demo_student()
    view.show_student(student)

if __name__ == "__main__":
    main()
