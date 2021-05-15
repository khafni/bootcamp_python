import functools
import numpy
import math

class TinyStatistician:
    def mean(x):
        return (functools.reduce(lambda a, b: a + b, x) / len(x))
    def percentile(arr, perc):
        arr.sort()
        res = []
        for x in arr:
            if x not in res:
                res.append(x)
        rank = (perc * (len(arr) + 1)) / 100
        if isinstance(rank, float):
            cmp_value = (arr[math.floor(rank) - 1] + arr[math.ceil(rank) - 1]) / 2.0
            v = arr[0]
            for x in arr:
                if (abs(x - cmp_value) < abs(v - cmp_value)):
                    v = x
            return v
        else:
            return arr[rank - 1]
    def median(arr):
        return float(TinyStatistician.percentile(arr, 50))
    def quartiles(arr, percentile):
        if percentile == 25:
            per = 1
        elif percentile == 75:
            per = 3
        arr.sort()
        i = 0
        for e in arr:
            i += 1
        if (i % (4 * per)) == 0:
            i = int(i/4 * per)
            return (float((arr[i - 1] + arr[i]) / 2))
        return float(arr[i//4 * per])
    def var(x):
        mu = TinyStatistician.mean(x)
        sum = 0
        for e in x:
            sum +=  math.pow((e - mu), 2)
        #sum = math.pow(sum, 2)
        #sum += math.pow((x[i] - mu), 2)
        res = sum / len(x)
        return res
    def std(x):
        return math.sqrt(TinyStatistician.var(x))
    

tstat = TinyStatistician()

arr = [1, 42, 300, 10, 59]




print(TinyStatistician.mean(arr))
print(TinyStatistician.median(arr))
print(TinyStatistician.quartiles(arr, 75))
print(TinyStatistician.var(arr))
print(TinyStatistician.std(arr))
#print(TinyStatistician.median(arr, 25))
#print(numpy.random.randn(1, 5))