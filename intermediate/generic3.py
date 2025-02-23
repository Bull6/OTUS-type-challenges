from typing import TypeVar

T = TypeVar('T', bound=int)  # Ограничиваем тип только int и его подклассы

def add(a: T) -> T:
    return a
