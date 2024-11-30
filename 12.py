coroutine = lambda f: (lambda *args, **kwargs: (gen := f(*args, **kwargs), next(gen))[0])


def test_coroutine():
    @coroutine
    def storage():
        values = set()
        was_there = False

        while True:
            val = yield was_there
            was_there = val in values
            if not was_there:
                values.add(val)

    st = storage()
    assert not st.send(42)
    assert st.send(42)
