import random

from time_it import TimeIt
from running_median import compute_median


def generate_samples(samples):
    return (random.randint(0, 1000) for _ in range(samples))


def performance_measurement(samples, window_size, mode='running', rounds=5):
    minimum, maximum, average = TimeIt(rounds, compute_median, window_size, mode=mode)(generate_samples, samples)
    print('{:10d} {:10d} {:10s} {:8.3f}ms {:8.3f}ms {:8.3f}ms'.format(
        samples, window_size, mode, minimum, maximum, average))


def do_performance_tests():
    testcases = []
    for samples in range(1, 100000, 10000):
        for window_size in range(1, samples, int(samples / 10) or 1):
            data = samples, window_size
            testcases.append(data)
    print('{:>10s} {:>10s} {:10s} {:>10s} {:>10s} {:>10s}'.format(
        'samples', 'window', 'mode', 'minimum', 'maximum', 'average'))
    for samples, window_size in testcases:
        performance_measurement(samples, window_size, 'running')
        performance_measurement(samples, window_size, 'naive')


if __name__ == "__main__":
    do_performance_tests()
