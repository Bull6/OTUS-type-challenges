from typing import TypeVar

T = TypeVar('T', int, str)  # Ограничиваем тип только int и str

def add(a: T, b: T) -> T:
    return a + b

# Valid cases
def test_valid_add_int():
    assert add(1, 2) == 3

def test_valid_add_str():
    assert add("hello", " world") == "hello world"

# Invalid cases (should fail type check)
import pytest
from typing import assert_type

@pytest.mark.xfail(strict=True)
def test_invalid_add_mixed():
    add(1, "hello")  # expect-type-error

@pytest.mark.xfail(strict=True)
def test_invalid_add_list():
    add(["a", "b"], ["c", "d"])  # expect-type-error

# Type assertion tests
def test_assert_types():
    assert_type(add(1, 2), int)
    assert_type(add("hello", " world"), str)
