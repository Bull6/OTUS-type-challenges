from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

def foo(name: str, age: int) -> None:
    # Function implementation
    print(f"Name: {name}, Age: {age}")

# Example usage
foo(name="Alice", age=30)
