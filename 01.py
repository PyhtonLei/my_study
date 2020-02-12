"""
监测 GitHub 项目更新并自动打开网页
"""

# api: https://api.github.com/repos/channelcat/sanic
# web_page https://github.com/channelcat/sanic

import requests
import webbrowser
import time
# 获取API所有信息
# json数据改为字典类型
api = "https://api.github.com/repos/channelcat/sanic"
all_info = requests.get(api).json()
web_page = "https://github.com/channelcat/sanic"
last_update = None
cur_update = all_info["updated_at"]
# print(cur_update)
while True:
    if not last_update:
        last_update = cur_update

    if last_update < cur_update:
        webbrowser.open(web_page)

    time.sleep(6000)
