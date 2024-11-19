class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = {}
        self._order = []

    def get(self, key):
        if key in self.cache:
            self._order.remove(key)
            self._order.append(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self._order.remove(key)
            self._order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                oldest_key = self._order.pop(0)
                del self.cache[oldest_key]
            self.cache[key] = value
            self._order.append(key)
