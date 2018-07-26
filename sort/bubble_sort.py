# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   bubble_sort.py 
# @Time:   2018/7/26 9:04

import random


def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


array = [random.randrange(1000) for i in range(10)]
print 'before sort:\n', array
print("-------final-------")
print bubble_sort(array)
