# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   heap_sort.py 
# @Time:   2018/7/26 10:34

####
#
# Python堆排序
# 将初始待排序关键字序列（R1，R2,......Rn）构建成大顶堆，为初始的无序区
# 将顶堆元素R1与最后一个元素Rn交换，此时得到的新的无序区（R1,R2,...Rn-1）和新的有序区（Rn）
# 由于交换后新的堆顶可能违反堆的性质，所以需要对当前无序区（R1,R2,......Rn-1）调整为新堆
# 然后再次将R1与无序区最后一个元素交换，得到和新的无序区（R1,R2......Rn-2）和新的有序区（Rn-1,Rn）
# 不断重复此过程知道有序区的元素为n-1，则整个排序过程完成
#
####

import random


def heap_sort(array):
    for start in range((len(array) - 2)//2, -1, -1):
        sift_down(array, start, len(array)-1)
    for end in range(len(array)-1, 0, -1):
        array[0], array[end] = array[end], array[0]
        sift_down(array, 0, end-1)
    return array


def sift_down(array, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and array[child] < array[child+1]:
            child += 1
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break


array = [random.randrange(100) for i in range(10)]
print(array)

print heap_sort(array)