__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

# 排序

def bubble_sort(seq):
    """冒泡排序"""
    for i in range(0, len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
        print(seq)
    return seq


def bubble_sort_plus(seq):
    """冒泡排序"""
    flag = False  # 设置一个flag，如果有一轮没有交换操作就说明已经有序了
    for i in range(0, len(seq)):
        flag = False
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
                flag = True
        if flag:
            return seq
    return seq


def select_sort(seq):
    """选择排序 每次找一个最小的元素交换，每一轮只需要交换一次"""
    n = len(seq)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if seq[min_idx] > seq[j]:
                min_idx = j
        if min_idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
    return seq


def insert_sort(seq):
    """每次挑选下一个元素插入已经排序的数组中,初始时已排序数组只有一个元素"""
    for i in range(1, len(seq)):
        val = seq[i]# save the value to be positioned
        pos = i# find the position where value fits in the ordered part of the list
        while pos > 0 and seq[pos - 1] > val:
            # Shift the items to the right during the search
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = val
    return seq



def quick_sort(list):
    """快速排序 """
    if len(list) < 2:
        return list
    else:
        mid = list[0]
        left = [i for i in list[1:] if i <= mid]
        right = [i for i in list[1:] if i > mid]
        fin = quick_sort(left) + [mid] + quick_sort(right)
        return fin


if __name__ == '__main__':
    a = [1, 67, 242, 5, 2, 3]

    print(bubble_sort(a))
    print(bubble_sort_plus(a))
    print(select_sort(a))
    print(quick_sort(a))
