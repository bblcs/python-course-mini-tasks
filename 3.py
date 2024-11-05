def read_matrix(s: str):
    return [[float(i) for i in line.split()] for line in s.split("|")]


def tests():
    assert read_matrix("1 2 | 3 4") == [[1.0, 2.0], [3.0, 4.0]]

    assert read_matrix("1.1 2.2 | 3.3 4.4") == [[1.1, 2.2], [3.3, 4.4]]

    assert read_matrix(
        "1 1 1 1 1 | 2 2 2 2 2 | 3 3 42 3 3 | 4 4 4 4 4 | 5 5 5 5 5"
    ) == [
        [1.0, 1.0, 1.0, 1.0, 1.0],
        [2.0, 2.0, 2.0, 2.0, 2.0],
        [3.0, 3.0, 42.0, 3.0, 3.0],
        [4.0, 4.0, 4.0, 4.0, 4.0],
        [5.0, 5.0, 5.0, 5.0, 5.0],
    ]

    print("all tests passed")


tests()
