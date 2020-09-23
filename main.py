import random

from running_median.example import compute_median


def generate_samples(samples):
    return (random.randint(0, 1000) for _ in range(samples))


def main(samples, window_size, check=False, display=1000):
    compute_median(generate_samples(samples), window_size, check, display)


if __name__ == "__main__":
    main(100000, 10000, False)
