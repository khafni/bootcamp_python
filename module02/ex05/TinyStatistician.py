import functools

class TinyStatistician:
    def mean(x):
        return (functools.reduce(lambda a, b: a + b, x) / len(x))
    def median(x):
        pass

print(TinyStatistician.mean([1, 2, 3, 4, 5]))
