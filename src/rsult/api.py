from .core import Result as Result
from .types import T, E


def unwrap(result: Result[T | None, E | None]) -> T | None:
    """Unwrap the result object.

    Args:
        result (Result): The result object.

    Returns:
        T: The response object.

    Raises:
        E: The error unwrapped from the result.
    """
    if result.error:
        raise result.error
    return result.response


def wrap(response: T) -> Result[T, None]:
    """Wrap the response object.

    Args:
        response (object): The response object.

    Returns:
        Result: The result object.
    """
    return Result(response=response)


def wrap_error(error: E) -> Result[None, E]:
    """Wrap the error object.

    Args:
        error (Exception): The error object.

    Returns:
        Result: The result object.
    """
    if not isinstance(error, Exception):  # pyright: ignore[reportUnnecessaryIsInstance]
        raise TypeError("error must be an instance of Exception")  # pyright: ignore[reportUnreachable]
    return Result(error=error)
