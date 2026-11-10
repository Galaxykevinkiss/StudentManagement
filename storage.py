import json
from student import Student


def save_students(students):
    data = []

    for student in students:
        data.append(student.to_dict())

    with open("out.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("保存成功！")


def load_students():
    try:
        with open("out.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        students = []

        for item in data:
            student = Student(
                item["name"],
                item["age"],
                item["score"]
            )
            students.append(student)

        print("读取成功！")
        return students

    except FileNotFoundError:
        print("文件不存在，使用空列表")
        return []