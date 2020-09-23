from ring import Ring


def median(s):
    """Returns the median of the _already__sorted list s"""
    size = len(s)
    index = size // 2
    return s[index] if size % 2 else (s[index] + s[index - 1]) / 2


class NaiveRunningMedian:
    """Minimal implementation of Running Median

    works perfectly fine but is slow for big windows"""

    def __init__(self, window_size):
        self._window = []
        self._capacity = window_size

    def insert(self, x):
        self._window.append(x)
        if len(self._window) > self._capacity:
            self._window = self._window[1:]
        return self

    def median(self):
        return median(sorted(self._window))


class SortedVector:
    """Keeps a sorteed list of all inserted elements"""
    def __init__(self):
        self._data = []

    def find_pos_(self, x):
        """Finds where given value is or should be"""
        (a, b) = (0, len(self._data))
        while a < b:
            m = (a + b) // 2
            if self._data[m] < x:
                a = m + 1
            else:
                b = m
        return a

    def insert(self, x):
        i = self.find_pos_(x)
        self._data[i:i] = [x]

    def remove(self, x):
        i = self.find_pos_(x)
        del self._data[i]

    def __getitem__(self, item): return self._data[item]
    def __len__(self): return len(self._data)


class RunningMedian:

    def __init__(self, window_size):
        self._ring = Ring(window_size)
        self._sorted = SortedVector()

    def insert(self, x):
        current = self._ring.insert(x)
        if current is not None:
            self._sorted.remove(current)
        self._sorted.insert(x)

    def median(self):
        return median(self._sorted)
