from typing import TypeVar, Callable, ParamSpec
from functools import wraps

T = TypeVar("T")
P = ParamSpec("P")

# Декоратор, сохраняющий сигнатуру функции
def decorator(func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a: int) -> int:
    return a
