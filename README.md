# RunningMedian.py

Efficient running median in plain Python

Have a look at the sibling project [RunningMedian.cpp](https://github.com/thomedes/RunningMedian.cpp)

This sub 100 lines file contains two different implementation of running
median:

## NaiveRunningMedian

Is what it's name says, a very simple simple implementation that can be
used with small windows or when simplicity is preferable to efficiency.

In the file it can be used as a comparison check against RunningMedian

## RunningMedian

This is the main implementation, it's run time for M sized window over a
N long sequence is O(N * log(M)).

To put it in numbers, see this table obtained with a Core i7:

|     N     |    M    |  time  |
|-----------|---------|--------|
|    10,000 |   1,000 |  0.2 s |
|   100,000 |  10,000 |  1.6 s |
| 1,000,000 | 100,000 | 45.1 s |

If you need to do your own speed tests just adjust
SAMPLES and WINDOW_SIZE and run the file.

# Usage

For a simple example have a look at the `main()` function:

```python
    w = RunningMedian(WINDOW_SIZE)

    for i in range(SAMPLES):
        sample = random.randint(0, 1000)

        w.insert(sample)
        wm = w.median()
        # Do something with wm
```
