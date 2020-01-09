# -*- utf-8 -*-
# @Time : 2020/1/9
# @Author : yaozh16
# @File : run.py 
# @Software: PyCharm
# @Description: 

import requests

if __name__ == "__main__":
    url = "http://202.112.51.130:28053"
    file_path = "01.png"
    sess = requests.session()
    sess.get(url)
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url=url+"/?poj=upload", files=files)
    with open("response.html", 'w', encoding="utf8") as f:
        f.write(response.text)
        f.close()