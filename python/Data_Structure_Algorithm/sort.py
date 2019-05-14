# coding: utf-8
import random
'''
Sort algorithm
'''


def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp

'''
def SortApi(func_name, data):
    command = '{}({})'.format(func_name, 'data')
    eval(command)
'''


def SortApi(func, data):
    func(data)


def QuickSort(data):
    def partition(data, left, right):
        i = left + 1
        j = right
        base = data[left]
        while(True):
            while data[i] < base and i != right:
                i += 1
            while data[j] > base and j != left:
                j -= 1
            if i >= j:
                break
            swap(data, i, j)
        swap(data, j, left)
        return j

    def _sort(data, left, right):
        if left >= right:
            return
        j = partition(data, left, right)
        _sort(data, left, j-1)
        _sort(data, j+1, right)
    random.shuffle(data)
    _sort(data, 0, len(data) - 1)


def InsertSort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
                swap(data, j, j - 1)


def BubbleSort(data):
    isSort = False
    for i in range(len(data) - 1, 0, -1):
        if isSort:
            break
        isSort = True
        for j in range(0, i):
            if data[j+1] < data[j]:
                isSort = False
                swap(data, j+1, j)


def SelectionSort(data):
    for i in range(len(data)-1):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        swap(data, min_index, i)


def MergeSort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    mid = len(seq) / 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = MergeSort(seq[:mid])
    right = MergeSort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


SORT_POOL = [QuickSort, InsertSort, BubbleSort, SelectionSort, MergeSort]
if __name__ == '__main__':
    data = [2, 4, 1, 3, 5]
    print(data)
    for func in SORT_POOL:
        ori_data = [i for i in data]
        func(ori_data)
        print('algorithm: {}\nresult: {}\n'.format(func.__name__, ori_data))
