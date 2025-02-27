from .core import Result as Result
from .api import unwrap as unwrap
from .api import wrap as wrap
from .api import wrap_error as wrap_error

if __name__ == "__main__":
    both = Result(response="derp", error=Exception("derp"))
    succeed = Result(response="derp")
    fail = Result(error=Exception("derp"))

    def print_result(result: Result):
        response, error = result
        print(type(response), type(error))

    print_result(both)
    print_result(succeed)
    print_result(fail)

    print(unwrap(succeed))
    print(unwrap(fail))
    print(unwrap(both))
