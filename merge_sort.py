def merge(array_left, array_right):
    if len(array_left) == 0:
        return array_right
    if len(array_right) == 0:
        return array_left

    result = []
    idx_left, idx_right = 0, 0

    while len(result) < len(array_left) + len(array_right):
        if idx_left == len(array_left):
            return result + array_right[idx_right:]

        if idx_right == len(array_right):
            return result + array_left[idx_left:]

        if array_left[idx_left] < array_right[idx_right]:
            result.append(array_left[idx_left])
            idx_left += 1
        else:
            result.append(array_right[idx_right])
            idx_right += 1

    return result


def merge_sort(array):
    if len(array) == 1:
        return array

    array_left, array_right = array[:len(array) // 2], array[len(array) // 2:]
    return merge(merge_sort(array_left), merge_sort(array_right))


print(merge_sort([2, 3, 4, 5, -1, -2, -3]))
