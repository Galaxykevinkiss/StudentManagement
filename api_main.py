from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import database as db

# 创建 FastAPI 应用
app = FastAPI()

# 初始化数据库
db.init_db()

# 学生数据模型
class Student(BaseModel):
    name: str
    age: int
    score: float



# 1. 查询所有学生
@app.get("/students")
def get_students():
    return db.get_all_students()


# 2. 根据 ID 查询学生
@app.get("/students/{student_id}")
def get_student(student_id: int):
     student=db.get_student(student_id)

     if student is None:
         raise HTTPException(
             status_code=404,
             detail="Student not found"
         )

     return student

# 3. 新增学生
@app.post("/students", status_code=201)
def create_student(student: Student):
    new_id = db.insert_student(
        student.name,
        student.age,
        student.score
    )

    return {
        "id": new_id,
        "name": student.name,
        "age": student.age,
        "score": student.score,
        "message": "Student created successfully"
    }

# 4. 修改学生信息
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    success = db.update_student(
        student_id,
        student.name,
        student.age,
        student.score
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student updated successfully",
        "student": db.get_student(student_id)
    }

# 5. 删除学生信息
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    success = db.delete_student(student_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }