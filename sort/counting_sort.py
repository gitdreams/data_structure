# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   counting_sort.py 
# @Time:   2018/7/26 15:59

import random

def counting_sort(arrays):
    bucket = [0] * (max(arrays)+1)
    for num in arrays:
        bucket[num] += 1
    i = 0
    for j in range(len(bucket)):
        while bucket[j] > 0:
            arrays[i] = j
            bucket[j] -=1
            i += 1
    return arrays


array = [random.randrange(100) for i in range(10)]
print array

print counting_sort(array)