import time
from wechat import Wechat


def test():
    print("打包")
    time.sleep(1)


if __name__ == '__main__':
    test()
    Wechat().chat()
