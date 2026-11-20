import sqlite3
from pathlib import Path

# 获取当前项目目录下的 student.db
DB_PATH = Path(__file__).resolve().parent / "student.db"


# 1. 创建数据库连接
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# 2. 初始化数据库和数据表
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        score REAL
    )
    """)

    conn.commit()
    conn.close()


# 3. 查询所有学生
def get_all_students():
    conn = get_connection()                   # 获取数据库连接
    cursor = conn.cursor()                    # 创建游标
    cursor.execute("SELECT * FROM students")  # 执行查询S
    rows = cursor.fetchall()                  # 获取所有查询结果
    conn.close()                              # 关闭数据库连接
    return [dict(row) for row in rows]        # 将查询结果转换为字典列表返回

# 4. 根据id查询学生
def get_student(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:     #若该id对应的学生不存在，row=None dict(None)会报错
        return None
    return dict(row)

# 5. 新增学生
def insert_student(name, age, score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO students (name, age, score) VALUES (?, ?, ?)""", (name, age, score))
    new_id = cursor.lastrowid  #取得数据库刚刚自动生成的学生 ID
    conn.commit()
    conn.close()
    return new_id

def update_student(id,name,age,score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE students SET name = ?, age = ?, score = ? WHERE ID=?""", (name, age, score, id))
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return affected_rows > 0

def delete_student(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM students WHERE ID = ?""", (id,))
    affected_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return affected_rows > 0

# 单独运行 database.py 时，初始化数据库
if __name__ == "__main__":
    init_db()
    print("数据库初始化成功！")
    print(get_all_students())
