from typing import ClassVar
import pytest

class Foo:
    """Hint: No need to write __init__"""
    bar: ClassVar[int]


# Valid case
def test_valid_case():
    Foo.bar = 42  # Should pass

# Invalid cases (should fail type check)
@pytest.mark.xfail(strict=True)
def test_invalid_case_string():
    Foo.bar = "hello"  # expect-type-error

@pytest.mark.xfail(strict=True)
def test_invalid_case_float():
    Foo.bar = 3.14  # expect-type-error
