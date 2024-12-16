import unittest
from unittest.mock import patch
import functools


def deprecated(*args, **kwargs):
    if len(args) == 1 and callable(args[0]):
        return deprecated()(args[0])

    since = kwargs.get("since", None)
    will_be_removed = kwargs.get("will_be_removed", None)

    def decorator(f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            message_template = "Warning: function {name} is deprecated"
            if since:
                message_template += f" since version {since}"
            if will_be_removed:
                message_template += f". It will be removed in version {will_be_removed}"
            else:
                message_template += ". It will be removed in future versions"
            message_template += "."

            print(message_template.format(name=f.__name__))
            return f(*args, **kwargs)

        return wrap

    return decorator


class TestDeprecatedDecorator(unittest.TestCase):
    @deprecated(since="1.0", will_be_removed="2.0")
    def func_with_both_versions(self):
        return "Function Executed"

    @deprecated(since="1.0")
    def func_with_since_only(self):
        return "Function Executed"

    @deprecated(will_be_removed="2.0")
    def func_with_will_be_removed_only(self):
        return "Function Executed"

    @deprecated
    def func_without_versions(self):
        return "Function Executed"

    def test_func_with_both_versions(self):
        with patch("builtins.print") as mocked_print:
            result = self.func_with_both_versions()
            mocked_print.assert_called_once_with(
                "Warning: function func_with_both_versions is deprecated since version 1.0. It will be removed in version 2.0."
            )
            self.assertEqual(result, "Function Executed")

    def test_func_with_since_only(self):
        with patch("builtins.print") as mocked_print:
            result = self.func_with_since_only()
            mocked_print.assert_called_once_with(
                "Warning: function func_with_since_only is deprecated since version 1.0. It will be removed in future versions."
            )
            self.assertEqual(result, "Function Executed")

    def test_func_with_will_be_removed_only(self):
        with patch("builtins.print") as mocked_print:
            result = self.func_with_will_be_removed_only()
            mocked_print.assert_called_once_with(
                "Warning: function func_with_will_be_removed_only is deprecated. It will be removed in version 2.0."
            )
            self.assertEqual(result, "Function Executed")

    def test_func_without_versions(self):
        with patch("builtins.print") as mocked_print:
            result = self.func_without_versions()
            mocked_print.assert_called_once_with(
                "Warning: function func_without_versions is deprecated. It will be removed in future versions."
            )
            self.assertEqual(result, "Function Executed")


if __name__ == "__main__":
    unittest.main()
