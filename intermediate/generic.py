from typing import TypeVar, List

T = TypeVar('T', int, float, str, List[str])  # Ограничиваем list до List[str]

def add(a: T, b: T) -> T:
    return a + b

# Valid cases
def test_valid_add_int():
    assert add(1, 2) == 3

def test_valid_add_str():
    assert add("hello", " world") == "hello world"

def test_valid_add_list():
    assert add(["a", "b"], ["c", "d"]) == ["a", "b", "c", "d"]

# Invalid cases (should fail type check)
import pytest
from typing import assert_type

@pytest.mark.xfail(strict=True)
def test_invalid_add_mixed():
    add(1, "hello")  # expect-type-error

# Type assertion tests
def test_assert_types():
    assert_type(add(1, 2), int)
    assert_type(add("hello", " world"), str)
    assert_type(add(["a", "b"], ["c", "d"]), List[str])  # Исправлено
