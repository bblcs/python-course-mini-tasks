import unittest
from io import StringIO
import sys


def format_table(benches, algs, results):
    if len(benches) == 0 or len(algs) == 0:
        print("not enough data")
        return
    header = f"| {'Benchmark':<10} | " + " | ".join(f"{alg:<10}" for alg in algs) + " |"
    separator = "|" + "-" * (len(header) - 2) + "|"
    rows = "\n".join(
        f"| {bench:<10} | " + " | ".join(f"{result:<10}" for result in row) + "  |"
        for bench, row in zip(benches, results)
    )
    print(f"{header}\n{separator}\n{rows}")


class TestFormatTable(unittest.TestCase):
    def setUp(self):
        self.fix_stdout = StringIO()
        sys.stdout = self.fix_stdout

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_format_table_basic(self):
        format_table(
            ["best case", "worst case"],
            ["quick sort", "merge sort", "bubble sort"],
            [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]],
        )
        expected = (
            "| Benchmark  | quick sort | merge sort | bubble sort |\n"
            "|----------------------------------------------------|\n"
            "| best case  | 1.23       | 1.56       | 2.0         |\n"
            "| worst case | 3.3        | 2.9        | 3.9         |\n"
        )
        self.assertEqual(self.fix_stdout.getvalue(), expected)

    def test_format_table_blank(self):
        format_table([], [], [])
        expected = "not enough data\n"
        self.assertEqual(self.fix_stdout.getvalue(), expected)

    def test_format_table_single(self):
        format_table(["average"], ["sample sort"], [[0.5]])
        expected = (
            "| Benchmark  | sample sort |\n"
            "|--------------------------|\n"
            "| average    | 0.5         |\n"
        )
        self.assertEqual(self.fix_stdout.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
