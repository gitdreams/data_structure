# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   binary.py 
# @Time:   2018/6/29 16:32

from stack import Stack


def binary(num):

    s = Stack()
    while num > 0:
        s.push(int(num % 2))
        num //= 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num


print(binary(233.6))
