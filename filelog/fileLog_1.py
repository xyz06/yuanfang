import time
import logging
from functools import wraps


# logging.basicConfig(level=logging.INFO,
#                     datefmt='%Y %m %d %H:%M:%S',
#                     filemode='a',
#                     filename='funcLog.log',
#                     format='[ %(asctime)s] %(funcName)s - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('[ %(asctime)s - %(levelname)s -文件路径%(pathname)s - %(lineno)d行]: %(message)s ', datefmt='%Y %m %d %H:%M:%S')
handler = logging.FileHandler('funcLog.log', encoding='utf-8')
handler.setFormatter(formatter)
logger.addHandler(handler)


def funcTime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        temp = func(*args, **kwargs)
        end = time.perf_counter()
        fTime = end - start
        logger.info("函数 %s ,耗时 %f , 返回的参数为 %s" % (func.__name__, fTime, temp))
        return temp

    return wrapper


@funcTime
def test(message='xyz'):
    print("hello world", message)
    return message


msg = test()
print("return %s" % msg)
