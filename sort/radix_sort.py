# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   radix_sort.py 
# @Time:   2018/7/26 16:24

import random


def radix_sort(arrays):
    mod = 10
    div = 1
    most_bit = len(str(max(arrays)))
    buckets = [[] for row in range(mod)]
    while most_bit:
        for num in arrays:
            buckets[num // div % mod].append(num)
        i = 0
        for bucket in buckets:
            while bucket:
                arrays[i] = bucket.pop(0)
                i += 1
        div *= 10
        most_bit -= 1
    return arrays


arrays = [random.randrange(100) for i in range(10)]
print(arrays)

print(radix_sort(arrays))
