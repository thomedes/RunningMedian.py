# RunningMedian.py

Efficient running median in plain Python

This sub 100 lines file contains two different implementation of running
median:

## NaiveRunningMedian

Is what it's name says, a very simple simple implementation that can be
used with small windows or when simplicity is preferable to efficiency.

In the file it can be used as a comparison check against RunningMedian

## RunningMedian

This is the main implementation, it's run time for M sized window over a
N long sequence is N*log(M). To put it in numbers, a Core i7 does 1K
window over 50K seq. in under a second or a 10K window over 100K sequence
in under two seconds. If you need to do your own speed tests just adjust
SAMPLES and WINDOW_SIZE and run the file.

# Usage

For a simple example have a look at the main() function:

```python
    w = RunningMedian(WINDOW_SIZE)

    for i in range(SAMPLES):
        sample = random.randint(0, 1000)

        w.insert(sample)
        wm = w.median()
        # Do something with wm
```
