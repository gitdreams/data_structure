# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   merge_sort.py 
# @Time:   2018/7/26 9:29

import random


def merge(left, right):
    i, j = 0, 0
    results = list()
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1
    results += left[i:]
    results += right[j:]
    return results


def merge_sort(array):
    # 结束递归条件
    if len(array) <= 1:
        return array
    length = len(array) // 2
    # 对切片递归调用归并排序函数进行排序
    left = merge_sort(array[:length])
    right = merge_sort(array[length:])
    # 合并分片
    return merge(left, right)


array = [random.randrange(100) for i in range(10)]
print 'before sort:\n', array
print("-------final-------")
print merge_sort(array)