import logging

# 1. 配置日志
logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# 2. 模拟程序启动
def start_program():
    print("学生管理系统启动")
    logging.info("学生管理系统启动成功")


# 3. 模拟添加学生
def add_student(name):
    print("学生添加成功！")
    logging.info(f"学生 {name} 添加成功")


# 4. 模拟成绩输入
def check_score(score):
    if score < 0 or score > 100:
        print("成绩不合法")
        logging.warning(f"成绩输入错误：{score}")
        return False

    print("成绩合法")
    return True


# 5. 程序入口
if __name__ == "__main__":

    start_program()

    add_student("Tom")

    check_score(120)

    check_score(90)