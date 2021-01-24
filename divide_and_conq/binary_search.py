import math


def binary_search(array, num):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == num:
            return mid

        if array[mid] > num:
            end = mid
        else:
            start = mid

    return math.nan


print(binary_search([1, 2, 3, 4, 5], 3))


def binary_search_recursive(array, num, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == num:
        return mid

    if array[mid] > num:
        return binary_search_recursive(array, num, start, mid)
    else:
        return binary_search_recursive(array, num, mid, end)


print(binary_search_recursive([1, 2, 3, 4, 5], 2, 0, 4))
