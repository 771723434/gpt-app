import time
import os
from wechat import Wechat
import gpt_env


def test():
    print("打包")
    time.sleep(1)


if __name__ == '__main__':
    os.putenv("openai_organization", gpt_env.openai_organization)
    os.putenv("openai_api_key", gpt_env.openai_api_key)
    test()
    Wechat().chat()
