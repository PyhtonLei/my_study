import requests
import webbrowser
import time

"""
练习：
Kenneth 今天 Star 了哪些库
Kenneth Reitz 是 Python 领域的大神级人物，并且在 Github 上非常活跃，
他的 Github 地址是：https://github.com/kennethreitz
试着用所学知识去发现 Kenneth 今天 Starred 了哪些库，
并且自动在浏览器中打开这些库的地址。
"""

"""
# 问题拆解
1. 如何获取用户star的库
2. 如何判断新项目的出现
3. 如何打开网页
4. 如何保持一段时间自动监测
"""

# api: https://api.github.com/users/kennethreitz/starred
# web_page: https://github.com/pypa/packaging
# web_page: https://github.com/MMcintire96/python_TinderAPI
# web_page: https://github.com/i["full_name"]

api = "https://api.github.com/users/PyhtonLei/starred"
all_info = requests.get(api).json()

id_list = []

for i in all_info:
    id_list.append(i["id"])
while True:
    all_info = requests.get(api).json()
    for i in all_info:
        if i["id"] not in id_list:
            id_list.append(i["id"])
            webbrowser.open("https://github.com/"+i["full_name"])
    time.sleep(60)
