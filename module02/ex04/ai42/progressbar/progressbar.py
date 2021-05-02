import time

def get_loading_bar(loading_bar_per, time, estimated_time, i, l):
    lbp = loading_bar_per
    #lbp = (lbp * 20) / 100
    bar_len = 30
    lbp = int(lbp)
    print("\rETA: {:.2f}s [{: >3}%]".format(estimated_time, lbp), end = '')
    lbp = float(lbp)
    lbp = (lbp * 30) / 100
    lbp = int(lbp)
    print("[{0: <{1}}]".format("".join(['=' for i in range(lbp)]) + '>' , bar_len), end='')
    print(" {}/{} | elapsed time {:.2f}s".format(i, l, time), end="")
    


def ft_progress(lst):
    start_t = time.time()
    end_t = time.time()
    l = len(lst)
    j = 0
    for i in lst:
        yield i
        j += 1
        et = time.time() - end_t
        end_t = time.time()
        get_loading_bar((j / l) * 100, end_t - start_t, et * l ,j, l)