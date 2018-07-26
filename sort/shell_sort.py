# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 16:31
# @Author  : li
# @File    : shell_sort.py

import random

def insertion_sort(array):

    for index in range(1, len(array)):
        # 记录当前元素值
        current_value = array[index]
        position = index
        # 只有在当前位置大于0，而且当前位置左边元素大于当前位置元素的时候
        # 才需要将当前位置左边的一个元素往右移动一位，并且当前位置往左移动一位
        while position > 0 and array[position-1] > current_value:
            array[position] = array[position-1]
            position -= 1
        # 直到直到一位元素不比current_value小，或者已经将左边所有元素比较完。
        # 记住左边永远是已经排好顺序的
        # 当将当前位置左边所有的元素都排好顺序之后，将current_value的值赋给当前位置元素
        array[position] = current_value
        print("insertion sort:", array)
    return array

# 希尔排序分组步长的取法是 len/2, (len/2)/2, ......


def shell_sort(array):

    step = int(len(array)/2)
    while step > 0:
        for index in range(0, len(array)):
            if index + step < len(array):
                current_value = array[index]
                if current_value > array[index+step]:
                    array[index], array[index + step] = array[index + step], array[index]
        print("shell sort :", array)
        step = int(step/2)
    return insertion_sort(array)

if __name__=="__main__":

    import time
    s = time.time()
    array = [random.randrange(10000+i) for i in range(10000)]
    print("source array", array)
    sort = shell_sort(array)
    print "----------希尔排序-----------"
    print(sort)
    t = time.time()
    print(t-s)