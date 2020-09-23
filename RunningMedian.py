#! /usr/bin/env python3

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
        self._ring = [None] * window_size
        self._head = 0
        self._sorted = SortedVector()

    def insert(self, x):
        current = self._ring[self._head]
        self._ring[self._head] = x
        self._head = (self._head + 1) % len(self._ring)

        if current is not None:
            self._sorted.remove(current)
        self._sorted.insert(x)

    def median(self):
        return median(self._sorted)


def main(samples, window_size, check=False, display=1000):
    import random

    running = RunningMedian(window_size)
    naive = NaiveRunningMedian(window_size)  # For comparison checks

    for i in range(samples):
        sample = random.randint(0, 1000)

        running.insert(sample)
        running_median = running.median()

        # Print something regularly
        if i % display == 0:
            print("%5d\t%d" % (i, running_median))

        # Check against naive implementation
        if check:
            naive.insert(sample)
            naive_median = naive.median()
            assert naive_median == running_median, "%d != %d" % (running_median, naive_median)


if __name__ == "__main__":
    main(100000, 10000, False)
