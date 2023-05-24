# 导入模块
import settings
from wxpy import *
from my_open_ai import Gpt


class Wechat(object):
    def chat(self):
        # 初始化机器人，扫码登陆
        bot = Bot(cache_path=True)
        # 向文件传输助手发送消息
        # bot.file_helper.send('Hello from wxpy!')
        my_friend = bot.friends().search(keywords=settings.wechat_friend_keyword)
        # print(my_friend)


        @bot.register(Friend, TEXT)
        def print_group_msg(msg):
            print(msg)
            content = Gpt().gpt_text(msg.text)
            # msg.forward(bot.file_helper, prefix='测试发言')
            # content = 'gpt回答'
            msg.chat.send(content)

        # 堵塞线程，并进入 Python 命令行
        embed()






