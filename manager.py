from student import Student


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("添加成功！")

    def show_students(self):
        for student in self.students:
            student.show_info()

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                student.show_info()
                return

        print("没有找到该学生")

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("删除成功！")
                return

        print("没有找到该学生")

    def calculate_average(self):
        if not self.students:
            print("当前没有学生")
            return

        total = 0

        for student in self.students:
            total += student.score

        average = total / len(self.students)

        print("平均成绩：", average)