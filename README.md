# Rsult

> Rsult (rust result = rs + result) is a python library for adding rust like `Result[T, E]` support to python.

## Background

In rust, rather than throw exceptions up some side channel, you return them directly as part of a functions response.
These responses are wrapped in what rust refers to as a `Result`.
`Result`'s are simple objects which contain either the result of the function call, or an exception which was raised by the function.

## Usage

There are many ways you can choose to use the rsult `Result` class.
The most common use is to just unpack the response into individual `error` and `response` variables.
However, the `unwrap()` functio can also be used much like unwrap in rust.
When called from a result that does not contain an error, `unwrap(result)` will return the `response` from the function.
If `unwrap(result)` is called with a result that contains an error, that error will be raised as an exception.

### Examples

```python
from rsult import Result, unwrap, wrap, wrap_error

class LessThanZeroError(Exception):
    pass

def add_numbers(x: int, y: int) -> Result[int, LessThanZeroError]:
    z = x + y
    if z < 0:
        return wrap_error(LessThanZeroError())
    return wrap(z)

# a regular call to the function that returns the response
error, answer = add_numbers(2, 2)
assert error is None
assert answer == 4

# a call to the function that results in an error
error, answer = add_numbers(2, -4)
assert type(error) is LessThanZeroError
assert answer is None

# unwrap can be used to throw the error, rather than unpacking the result
result = add_numbers(2, -4)
answer = unwrap(result)  # <-- LessThanZeroError gets throw
```

## Authors

- [PattyC (schlerp)](https://github.com/schlerp)
