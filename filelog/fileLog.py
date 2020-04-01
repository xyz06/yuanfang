import time
from functools import wraps


def logFile(logfile="funcTime.log"):


    def funcTime(func):
        @wraps(func)
        def wrapper():
            start = time.perf_counter()
            func()
            end = time.perf_counter()
            fTime = end - start
            log = "[" + time.asctime(time.localtime(time.time())) +"]"
            log += (" 函数: %s  耗时 %f" % (func.__name__, fTime))
            print(log)
            with open(logfile, 'a', encoding='utf-8') as f:
                f.write(log + '\n')
        return wrapper
    return funcTime


@logFile()
def test():
    print("hello world")


test()