def insertion_sort(array, compare_fn):
    """
    :param array: array of numbers or comparable objects
    :param compare_fn: function that compares two objects - a1 and a2, a1 < a2 returns -1, a1 == a2 returns 0 and
                        a1 > a2 returns 1
    :return: sorted copy of array
    """
    result = [x for x in array]  # clone

    for i in range(1, len(array)):
        j = i

        # break if j is less than 1 since we would index -1 in array
        while j >= 1 and compare_fn(result[j], result[j - 1]) < 0:
            result[j], result[j - 1] = result[j - 1], result[j]  # python swap expression
            j -= 1  # decrease j

    return result


def compare_fn(a1, a2):  # example of compare function - simple number comparison
    if a1 == a2:
        return 0
    return -1 if a1 < a2 else 1


unsorted_array = [-1, 2, 3, 4, 1, -2, 15, 123, 12, 33, 32, 2]  # example array

result = insertion_sort(unsorted_array, compare_fn)  # get sorted array

print('Array: {}'.format(unsorted_array))
print('Sorted result: {}'.format(result))
