# -*- coding: utf-8 -*-
'''
排序算法
'''

def QuickSort(nums):
    def _sort(nums, l, h):
        j = partition(nums, l, h)
        _sort(nums, l, j)
        _sort(nums, j+1, h)
    def partition(nums, l, h):
        i = l
        j = h+1
        v = nums[l]
        while True:
            while nums[i] < v and i != j:
                i += 1
            while nums[j] > v and i != j:
                j += 1
        return j