import os
import openai

openai.organization = "YOUR organization"
openai.api_key = "YOUR API KEY"
# openai.Model.list()

class Gpt(object):
    def gpt_text(self, msg):
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}]
        )
        content = resp['choices'][0]['message']['content']
        print("openAi content: {}".format(content))
        # print(msg)
        # context = msg
        return content
    # print(resp)

    def gpt_image(self, msg, format='url'):
        resp = openai.Image.create(prompt=msg, n=1, size="1024x1024", response_format=format)
        data = resp['data'][0][format]
        return data
# resp = openai.Image.create(prompt="狗狗拿铲子的漫画", n=1, size="1024x1024", response_format="b64_json")
# print(resp)
# import base64
# import io
# import image
# def open_image(img):
#     image = io.BytesIO(img)
#     print(image)
#     image = image.open(image)
#     img.show()
# data = ""
# def base64_to_image(str):
#     res=str.split(',')[1]
#     img = base64.b64decode(res)
#     with open("dog.jpg", 'wb') as png:
#         png.write(img)
# base64_to_image(base64.b64decode(data))
