from collections.abc import Iterator
from typing import override

from .types import T
from .types import E


class Result[T, E]:
    """A class to represent the result of an operation.

    Attributes:
        response (object): The response object.
        error (Exception): The error object.
    """

    response: T | None
    error: E | None

    def __init__(self, *, response: T | None = None, error: E | None = None):
        self.response = response
        self.error = error

    def __iter__(self) -> Iterator[T | E | None]:
        return iter((self.response, self.error))

    def __bool__(self) -> bool:
        return self.error is None

    @override
    def __str__(self) -> str:
        return f"Result(response={self.response}, error={self.error})"
