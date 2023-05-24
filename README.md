# gpt-app
gpt app

First,integrated wechat message auto reply by gpt3.5, env variables are completed later.


部署过程：

1)pip install -r requirements.txt

2)gpt配置在gpt_env.py中，

  openai_organization = "YOUR organization"
  
  openai_api_key = "YOUR API KEY"
  
  
  微信好友过滤在settings.py添加，
  
  wechat_friend_keyword = ["机器人", "蜡笔"]

2)python app.py

3)授权扫码登陆


待完成：

1)目前通过好友进行过滤应答，该部分后续完善 ---- 已完成

2)自动回答图片功能后续完善，调用gpt代码已完成


> Don't spray if you don't like it 

> Welcome to provide advice 

> Thanks 
