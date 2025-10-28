from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name : str
    age: Optional[int] = 32
    cgpa: float = Field(gt=0 , lt=10 , default=8.5, description="CGPA of the student")

new_student = Student({'name': 'Hammad'})
new_student = Student(Optional({'age': 22}))

student=Student(**new_student)

print(new_student) 