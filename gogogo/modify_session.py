# -*- utf-8 -*-
# @Time : 2020/1/10
# @Author : yaozh16
# @File : modify_session.py 
# @Software: PyCharm
# @Description: 

if __name__ == "__main__":
    with open("IiMfvlUILZgzUabnxxWU.png",'rb') as f:
        data = f.read()

    data_modified = data[:41]+ b'\x02' + data[42:-5] + b'admin'
    print(data)
    print(data_modified)
    with open("session.png",'wb') as f:
        f.write(data_modified)
        f.close()