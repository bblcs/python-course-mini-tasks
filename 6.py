def flatten(lis: list, depth=1) -> list:
    return [item for sublist in lis for item in (flatten(sublist, depth - 1) if isinstance(sublist, list) and depth > 0 else [sublist])]


def test_flatten_depth_0():
    assert flatten([1, [2, 3], [4, [5, 6]]], depth=0) == [1, [2, 3], [4, [5, 6]]]


def test_flatten_depth_1():
    assert flatten([1, [2, 3], [4, [5, 6]]], depth=1) == [1, 2, 3, 4, [5, 6]]


def test_flatten_depth_2():
    assert flatten([1, [2, 3], [4, [5, 6]]], depth=2) == [1, 2, 3, 4, 5, 6]


def test_flatten_depth_3():
    assert flatten([1, [2, [3, [4, 5]], 6], 7], depth=3) == [1, 2, 3, 4, 5, 6, 7]


def test_flatten_with_non_list_elements():
    assert flatten(["a", ["b", "c"], ["d", ["e", "f"]]], depth=1) == [
        "a",
        "b",
        "c",
        "d",
        ["e", "f"],
    ]


def test_flatten_empty_list():
    assert flatten([], depth=1) == []


def test_flatten_list_of_empty_lists():
    assert flatten([[], [[]], [[], []]], depth=2) == []


def test_flatten_no_depth_specified():
    assert flatten([1, [2, [3, [4, 5]], 6], 7]) == [
        1,
        2,
        [3, [4, 5]],
        6,
        7,
    ]


def test_flatten_negative_depth():
    assert flatten([1, [2, 3], [4, [5, 6]]], depth=-1) == [1, [2, 3], [4, [5, 6]]]


def test_flatten_large_depth():
    assert flatten([1, [2, [3, [4, [5, [6, 7]]]]]], depth=10) == [1, 2, 3, 4, 5, 6, 7]
