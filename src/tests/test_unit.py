from rsult import Result, unwrap, wrap, wrap_error


class TestRsult:
    def test_result(self):
        both = Result(response="derp", error=Exception("derp"))
        succeed: Result[str, None] = Result(response="derp")
        fail: Result[None, Exception] = Result(error=Exception("derp"))

        assert both.response == "derp"
        assert type(both.error) is Exception
        assert both.error.args[0] == "derp"

        assert succeed.response == "derp"
        assert succeed.error is None

        assert fail.response is None
        assert type(fail.error) is Exception
        assert fail.error.args[0] == "derp"

    def test_unwrap(self):
        succeed: Result[str, None] = Result(response="derp")
        fail: Result[None, Exception] = Result(error=Exception("derp"))

        assert unwrap(succeed) == "derp"  # pyright: ignore[reportArgumentType]
        try:
            unwrap(fail)  # pyright: ignore[reportArgumentType]
        except Exception as e:
            assert e.args[0] == "derp"

    def test_bool(self):
        succeed: Result[str, None] = Result(response="derp")
        fail: Result[None, Exception] = Result(error=Exception("derp"))

        assert bool(succeed) is True
        assert bool(fail) is False

    def test_str(self):
        succeed: Result[str, None] = Result(response="derp")
        fail: Result[None, Exception] = Result(error=Exception("derp"))

        assert str(succeed) == "Result(response=derp, error=None)"
        assert str(fail) == "Result(response=None, error=derp)"

    def test_iter(self):
        succeed: Result[str, None] = Result(response="derp")
        fail: Result[None, Exception] = Result(error=Exception("derp"))

        assert list(succeed) == ["derp", None]
        assert list(fail)[0] is None
        assert type(list(fail)[1]) is Exception
        assert list(fail)[1] is not None

    def test_result_unpacks(self):
        response, error = Result(response="derp", error=Exception("derp"))

        assert response == "derp"
        assert type(error) is Exception
        assert error.args[0] == "derp"

    def test_wrap(self):
        result = wrap("derp")

        assert result.response == "derp"
        assert result.error is None

    def test_wrap_error(self):
        result = wrap_error(Exception("derp"))

        assert result.response is None
        assert type(result.error) is Exception
        assert result.error.args[0] == "derp"

    def test_wrap_error_type_error(self):
        try:
            _ = wrap_error("derp")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType,reportUnknownVariableType]
        except TypeError as e:
            assert e.args[0] == "error must be an instance of Exception"
