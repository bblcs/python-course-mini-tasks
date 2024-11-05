def convert(a: list, b: list):
    r = []
    for i in range(min(map(len, [a, b]))):
        r.append((a[i], b[i]))
    return r


def tests():
    assert convert([], []) == []
    assert convert([], [1, 2]) == []
    assert convert("ab", [1, 2, 3]) == [("a", 1), ("b", 2)]
    assert convert([1, 2, 3], ["a", "b"]) == [(1, "a"), (2, "b")]

    print("all tests passed")


tests()
