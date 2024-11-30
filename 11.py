cycle = lambda iterable: (item for _ in iter(int, 1) for item in iterable)
chain = lambda *iterables: (item for iterable in iterables for item in iterable)
take = lambda iterable, n: [x for _, x in zip(range(n), iterable)]


def test_chain():
    assert list(chain([1, 2, 3], ["a", "b"], [42, 13, 7])) == [
        1,
        2,
        3,
        "a",
        "b",
        42,
        13,
        7,
    ]


def test_cycle():
    assert take(cycle([1, 2, 3]), 10) == [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
