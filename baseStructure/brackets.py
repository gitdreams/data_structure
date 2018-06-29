# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   brackets.py 
# @Time:   2018/6/24 21:29


from stack import Stack


def par_checker(symbolString):
    s = Stack()
    balanced = True
    for item in symbolString:
        if item == '(':
            s.push(item)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
    if balanced and s.is_empty():
        return True
    else:
        return False


print(par_checker("()))))"))
