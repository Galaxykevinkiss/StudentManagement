import logging
from student import Student
from manager import StudentManager
from storage import save_students, load_students


def main():
    manager = StudentManager()

    manager.students = load_students()

    while True:
        print("\n========== 学生管理系统 ==========")
        print("1. 添加学生")
        print("2. 显示学生")
        print("3. 查询学生")
        print("4. 删除学生")
        print("5. 计算平均成绩")
        print("6. 保存学生信息")
        print("0. 退出系统")

        choice = input("请输入操作：")

        if choice == "1":
            name = input("请输入姓名：")
            age = int(input("请输入年龄："))
            score = float(input("请输入成绩："))

            student = Student(name, age, score)
            manager.add_student(student)

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            name = input("请输入查询姓名：")
            manager.find_student(name)

        elif choice == "4":
            name = input("请输入删除姓名：")
            manager.delete_student(name)

        elif choice == "5":
            manager.calculate_average()

        elif choice == "6":
            save_students(manager.students)

        elif choice == "0":
            save_students(manager.students)
            print("退出系统")
            break

        else:
            print("输入错误，请重新选择")


if __name__ == "__main__":
    main()