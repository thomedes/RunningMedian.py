from median import RunningMedian, NaiveRunningMedian


def compute_naive_median(samples, window_size, display):
    naive = NaiveRunningMedian(window_size)
    for counter, sample in enumerate(samples):
        naive.insert(sample)
        naive_median = naive.median()
        # Print something regularly
        if display and counter % display == 0:
            print("%5d\t%d" % (counter, naive_median))


def compute_median(samples, window_size, check=False, display=None, mode='running'):
    """
    Given a sequence of samples, and a window_size, compute the running median until the data is exhausted
    Compare to the naive running median if check is True
    Display the running media every "display" rounds
    """
    running = RunningMedian(window_size)
    naive = NaiveRunningMedian(window_size)
    if mode == 'naive':
        compute_naive_median(samples, window_size, display)
        return
    for counter, sample in enumerate(samples):
        running.insert(sample)
        running_median = running.median()
        # Print something regularly
        if display and counter % display == 0:
            print("%5d\t%d" % (counter, running_median))
        # Check against naive implementation
        if check:
            naive.insert(sample)
            naive_median = naive.median()
            assert naive_median == running_median, "%d != %d" % (running_median, naive_median)
