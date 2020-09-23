class Ring:

    def __init__(self, size):
        self._ring = [None] * size
        self._head = 0

    def __len__(self):
        return len(self._ring)

    def insert(self, value):
        current = self._ring[self._head]
        self._ring[self._head] = value
        self._head = (self._head + 1) % len(self._ring)
        return current
