def cycle(iterable):
    not_memory_efficient = list(iterable)
    if not not_memory_efficient:
        return
    while True:
        yield from not_memory_efficient


def chain(*iterables):
    return (item for iterable in iterables for item in iterable)


def take(iterable, n):
    return [x for _, x in zip(range(n), iterable)]


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


def test_infty():
    assert take(cycle(chain([1])), 10) == [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    ]
