class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("成绩：", self.score)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "score": self.score
        }

    def introduce(self):
        print(f"大家好，我叫{self.name}，今年{self.age}岁")
