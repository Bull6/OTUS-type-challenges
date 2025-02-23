from typing import TypeVar, Self

T = TypeVar("T", bound="Foo")

class Foo:
    def return_self(self: T) -> T:
        return self
