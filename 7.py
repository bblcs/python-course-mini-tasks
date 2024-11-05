import unittest
from unittest.mock import patch
import functools


def deprecated(since=None, will_be_removed=None):
    def decorator(f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            if since is not None and will_be_removed is not None:
                fs = f"Warning: function {f.__name__} is deprecated since version {since}. It will be removed in version {will_be_removed}."
            elif since is None and will_be_removed is not None:
                fs = f"Warning: function {f.__name__} is deprecated. It will be removed in version {will_be_removed}."
            elif since is not None and will_be_removed is None:
                fs = f"Warning: function {f.__name__} is deprecated since version {since}. It will be removed in future versions."
            else:
                fs = f"Warning: function {f.__name__} is deprecated. It will be removed in future versions."
            print(fs)
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

    @deprecated()
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
