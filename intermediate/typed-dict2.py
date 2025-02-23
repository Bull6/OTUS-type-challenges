from typing import TypedDict


class Student(TypedDict, total=False):
    name: str
    age: int
    school: str