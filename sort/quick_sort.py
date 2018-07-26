# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 9:37
# @Author  : li
# @File    : quick_sort.py

import random

def quick_sort(array, left, right):
    """
    :param array: 待排序数据
    :param left: 左边下标
    :param right: 右边下标
    :return:
    """

    if left > right:
        return
    low = left
    hight = right
    key = array[low]

    while low < hight:
        while low < hight and array[hight] > key:
            # 只要hight下标的数据比key大，hight就往前走
            hight -= 1
        array[low] = array[hight]
        array[hight] = key
        while low < hight and array[low] <= key:
            # 只要low的数据比key小或者等于key，low就往后走
            low += 1
        array[hight] = array[low]
        array[low] = key
    print(array)

    quick_sort(array, left, low-1)
    quick_sort(array, low+1, right)

if __name__=="__main__":
    array = [random.randrange(10000+i) for i in range(10)]
    # array = [8,4,1, 14, 6, 2, 3, 9,5, 13, 7,1, 8,10, 12]
    print("before sort:", array)
    quick_sort(array, 0, len(array) - 1)

    print("-------final-------")
    print(array)
