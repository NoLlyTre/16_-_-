class ConsoleView:
    def show_welcome(self):
        print("Добро пожаловать в Личный кабинет")

    def show_student(self, student):
        print(f"Студент: {student.first_name} {student.last_name}")
