__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

# 合并两个有序列表


# 尾递归
def _recursion_merge_sort2(l1, l2, tmp: list):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)


def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])


# 循环算法
def loop_merge_sort(l1, l2):
    c = []
    while l1 and l2:
        if l1[0] < l2[0]:
            c.append(l1[0])
            del l1[0]
        else:
            c.append(l2[0])
            del l2[0]
    c.extend(l1)
    c.extend(l2)
    return c


# pop
def merge_sortedlist(l1, l2):
    c = []

    while l1 and l2:
        if l1[0] >= l2[0]:
            c.append(l2.pop(0))
        else:
            c.append(l1.pop(0))

    while l1:
        c.append(l1.pop(0))

    while l2:
        c.append(l2.pop(0))

    return c


if __name__ == '__main__':
    a = [1, 2, 3, 7]
    b = [3, 4, 5]
    print(loop_merge_sort(a, b))
    # print(recursion_merge_sort2(a, b))
    # print(merge_sortedlist(a, b))
