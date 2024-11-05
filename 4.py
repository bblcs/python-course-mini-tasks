import unittest


def rev(d: dict):
    r = {}
    for v in d.values():
        keys = tuple(filter(lambda x: d[x] == v, d.keys()))
        r.update({v: keys} if len(keys) > 1 else {v: keys[0]})
    return r


class AdvancedTests(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(TypeError):
            rev({[1]: [1]})


def tests():
    assert rev({}) == {}
    assert rev({"aa": "bb"}) == {"bb": "aa"}
    assert rev({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {
        97832: ("Ivanov", "Kuznecov"),
        55521: "Petrov",
    }
    unittest.main(exit=False)
    print("all tests passed")


tests()
