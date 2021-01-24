def partition(array, low, high):
    """
    :param array: array to be sorted
    :param low: start of the array
    :param high: end of the array (inclusive)
    :return:
    """

    pivot = array[high]

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # swap items on i and j indexes
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, start, end):
    if len(array) == 1:
        return array

    if start >= end:
        return

    partition_idx = partition(array, start, end)
    quick_sort(array, start, partition_idx - 1)
    quick_sort(array, partition_idx + 1, end)

arr= [2, 3, 4, 5, 1, 2, 3]
quick_sort(arr, 0, 6)
print(arr)
