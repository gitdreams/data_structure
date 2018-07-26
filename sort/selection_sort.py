# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 8:38
# @Author  : li
# @File    : selection_sort.py

import random

# 迭代选择排序
def selection_sort(array):

    for j in range(0, len(array)):
        small_value_index = j
        for i in range(j, len(array)):
            if array[i] < array[small_value_index]:
                small_value_index = i
        array[j], array[small_value_index] = array[small_value_index], array[j]
    return array

# 递归选择排序
def selection_sort_rec(array, n):

    if n == 0:
        return

    max_value_index = n
    for i in range(0, n):
        if array[i] > array[max_value_index]:
            max_value_index = i
    array[n], array[max_value_index] = array[max_value_index], array[n]
    selection_sort_rec(array, n-1)
    return array

if __name__=="__main__":

    array = [random.randrange(10000+i) for i in range(10)]
    print(array)
    print("------------选择排序（非递归）--------------")
    print(selection_sort(array))
    print("------------选择排序（递归）--------------")
    print(selection_sort_rec(array, len(array)-1))
