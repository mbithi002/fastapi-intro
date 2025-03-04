from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


students = {
    1: {
        "name": "John",
        "age": 20,
        "grade": 90
    },
    2: {
        "name": "Jane",
        "age": 21,
        "grade": 85
    },
    3: {
        "name": "Bob",
        "age": 21,
        "grade": 95
    }
}

class Student(BaseModel):
    name: str
    age: int
    grade: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[int] = None

@app.get("/")
def index():
    return {
        "message" : "Hello, world"
    }

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    if student_id in students:
        return{
            "student": [student_id]
        }
        
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {
            "error": "student ID already taken"
        }
    student[student_id] = student
    return {
        "Message": "student created successfully",
        "data": students
    }
    
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {
            "error": "student not found"
        }
    if student.name is not None:
        students[student_id]['name'] = student.name
    if student.age is not None:
        students[student_id]['age'] = student.age
    if student.grade is not None:
        students[student_id]["grade"] = student.grade
    
    return {
        "message": "student updated successfully",
        "data": students[student_id]
    }
    
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {
            "message": "student not found"
        }
    del students[student_id]
    return {
        "message": "student deleted successfully",
        "data": students
    }
    
@app.get("/get-by-name/{student_id}")
def get_by_name(*, student_id: int, name: Optional[str]):
    if student_id in students:
        if students[student_id]["name"] == name:
            return {
                "data": students[student_id]
            }
            
    return {
        "message": "student not found"
    }
    
@app.get("/get-by-age")
def get_by_age(*, age: int):
    result = []
    for index in students:
        if students[index]["age"] == age:
            result.append(students[index])
            
    return {
        "data": result
    }