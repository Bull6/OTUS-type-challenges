from typing import TypedDict, NotRequired

class Person(TypedDict):
    name: str  # Required
    age: NotRequired[int]
    gender: NotRequired[str]
    address: NotRequired[str]
    email: NotRequired[str]