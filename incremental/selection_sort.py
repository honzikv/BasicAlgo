import math


def selection_sort(array, compare_fn):
    result = [x for x in array]

    for idx in range(0, len(result)):
        min_val = result[idx]  # minimum value
        min_idx = idx  # index of element with minimum value

        for i in range(idx + 1, len(result)):  # iterate over every index
            if compare_fn(result[i], min_val) < 0:
                min_val = result[i]
                min_idx = i

        result[idx], result[min_idx] = result[min_idx], result[idx]  # swap minimum with index

    return result


def compare_fn(a1, a2):
    if a1 == a2: return 0
    return -1 if a1 < a2 else 1


array = [-1, -2, -3, -4, 4, 5, 3, 2, 1]
print(selection_sort(array, compare_fn))
