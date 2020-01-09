# -*- utf-8 -*-
# @Time : 2020/1/8
# @Author : yaozh16
# @File : md5.py 
# @Software: PyCharm
# @Description: 

from hashlib import md5
from string import ascii_letters,digits
from itertools import permutations
from time import time
all_letters=ascii_letters+digits+'.,;'
def decrypt_md5(md5_value):
    md5_value=md5_value.lower()
    for k in range(8,10):
        for item in permutations(all_letters,k):
            item=''.join(item)
            if md5(item.encode()).hexdigest()[:4]==md5_value:
                print(md5_value + '==>' + item)
                return item
if __name__ == "__main__":
    md5_value = 'fffd'
    start = time()
    result = decrypt_md5(md5_value)