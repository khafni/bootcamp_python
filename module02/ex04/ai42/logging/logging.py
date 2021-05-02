import time
from random import randint

def log(func):
    def wrap_fun(*args, **kwargs):
        t1 = time.time()
        f = open("machine.log", "a")
        result = func(*args, **kwargs)
        t2 = time.time()
        str = "(cmaxtime)Running: {:20}".format(func.__name__)
        r_t = (t2 - t1)
        if r_t > 1:
            str += "[ exec-time = {:.3f} s ]".format(r_t)
        else:
            str += "[ exec-time = {:.3f} ms ]".format(r_t * 1000)
        f.write(str)
        f.write("\n")
        f.close()
        return result
    return wrap_fun