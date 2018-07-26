# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   bucket_sort.py 
# @Time:   2018/7/26 16:09

from insertion_sort import insertion_sort
import random


def bucket_sort(arrays, defaultBucketSize=5):
    max_Val, min_Val = max(arrays), min(arrays)
    bucket_Size = defaultBucketSize
    bucket_Count = (max_Val - min_Val)
    buckets = list()
    for i in range(bucket_Count):
        buckets.append(list())
    for num in arrays:
        buckets[(num-min_Val) // bucket_Size].append(num)
    newarray = list()
    for bucket in buckets:
        insertion_sort(bucket)
        newarray.extend(bucket)
    return newarray


arrays = [random.randrange(100) for i in range(10)]
print(arrays)
print("final")
print bucket_sort(arrays)