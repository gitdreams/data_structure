# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   symbol.py 
# @Time:   2018/6/29 15:32

from stack import Stack


def par_checker(symbol_string):

    balanced = True
    s = Stack()
    index = 0
    for item in symbol_string:
        if item in "([{":
            s.push(item)
        else:
            if s.is_empty():
                balanced = False
            else:
                close = s.pop()
                if not mactches(close, item):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def mactches(item, close):
    items = "([{"
    closes = ")]}"
    return items.index(item) == closes.index(close)


print(par_checker("(({[]}))[]"))
