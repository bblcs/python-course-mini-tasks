import unittest
from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity=16):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return None
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache()

    def test_put_get_item(self):
        self.cache.put("key1", "value1")
        self.assertEqual(self.cache.get("key1"), "value1")

    def test_put_update_value(self):
        self.cache.put("key1", "value1")
        self.cache.put("key1", "value2")
        self.assertEqual(self.cache.get("key1"), "value2")

    def test_get_nonexistent_value(self):
        self.assertEqual(self.cache.get("nonexistent"), None)

    def test_cache_exceeds_capacity(self):
        for i in range(17):
            self.cache.put(f"key{i}", f"value{i}")
        self.assertIsNone(self.cache.get("key0"))

    def test_cache_order_updates_correctly(self):
        for i in range(5):
            self.cache.put(f"key{i}", f"value{i}")
        self.cache.get("key0")
        self.assertEqual(next(iter(self.cache)), "key1")


if __name__ == "__main__":
    unittest.main()
