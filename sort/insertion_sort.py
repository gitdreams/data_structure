# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 16:38
# @Author  : li
# @File    : insertion_sort.py

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
        # print(array)
    return array

if __name__=="__main__":

    array = [random.randrange(10000+i) for i in range(10)]
    sort = insertion_sort(array)
    print "-------------插入排序之后----------------"
    print sort