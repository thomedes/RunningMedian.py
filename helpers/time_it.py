import time


class TimeIt:

    def __init__(self, rounds, func, *args, **kwargs):
        self._rounds = rounds
        self._func = func
        self._args = args
        self._kwargs = kwargs
        if rounds <= 0:
            raise ValueError('We need a positive number of rounds')

    def __call__(self, prepare=None, *args):
        measurements = []
        all_args = self._args
        for _ in range(self._rounds):
            if prepare:
                data = prepare(*args)
                all_args = (data, *self._args)
            start = time.time()
            self._func(*all_args, **self._kwargs)
            elapsed = time.time() - start
            measurements.append(elapsed)
        minimum, maximum, average = min(measurements), max(measurements), sum(measurements) / len(measurements)
        return minimum, maximum, average
