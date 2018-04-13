__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

def binary_search(sorted_seq, item):
    """ 实现标准库中的bisect.bisect_left """
    low = 0
    high = len(sorted_seq) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_seq[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid
    return None


if __name__ == '__main__':
    l = [1, 2, 3, 5, 7]

    print(binary_search(l, 3))
