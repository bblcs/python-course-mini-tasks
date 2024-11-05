def specialize(f, *args, **kwargs):
    return lambda *nargs, **nkwargs: f(*(args + nargs), **(kwargs | nkwargs))


def f(a, b, c=0, d=0):
    return a + b + c + d


def test_no_args():
    t = specialize(f)
    assert t(1, 2) == 3
    assert t(1, 2, c=3) == 6
    assert t(1, 2, d=4) == 7


def test_args():
    t = specialize(f, 1, 2)
    assert t() == 3
    assert t(3) == 6
    assert t(3, 4) == 10


def test_kwargs():
    t = specialize(f, c=3, d=4)
    assert t(1, 2) == 10
    assert t(1, 2, c=5) == 12
    assert t(1, 2, d=5) == 11


def test_mix():
    t = specialize(f, 1, d=4)
    assert t(2) == 7
    assert t(2, c=3) == 10
    assert t(2, 3, d=5) == 11


def test_overwriting_kwargs():
    t = specialize(f, c=3, d=4)
    assert t(1, 2, c=5, d=1) == 9
