import math
from typing import List


def linear_partition_problem(array: List[int], num_partitions: int) -> List[List]:
    """
    :param array: sequence of positive integers S = { s1, s2, s3, .., sn }
    :param num_partitions: k - maximum number of partitions to divide the array into
    :return: list of partitions
    """

    array = [None] + array  # prepend so that we can index array from 1
    n, k = len(array), num_partitions

    # Create n x k table where n is number of elements in array and k is number of partitions
    # Table is (n + 1) x (k + 1) so that it is indexable from 1st element due to math formulas
    # Table is referenced as "M" - matrix
    # Column in the table corresponds to number of parts - index 1 represents a single partition ...
    # Each row in the table corresponds to number of items - index 1 represents an array with only one element ...
    table = [[None for _ in range(k + 1)] for _ in range(n)]

    # Path for to create the result
    path = [[None for _ in range(k + 1)] for _ in range(n)]

    # We can calculate trivial values such as k = 1 or n = 1
    # M(1, k) = s1
    for i in range(1,
                   k + 1):  # Calculate total cost for all "ks" if the number of elements in the array is equal to one
        table[1][i] = array[1]
    for i in range(1, n):  # Calculate total cost for k = 1 if the number of elements in the array is increasing by one
        # i.e calculate, M(1,1), M(2,1), M(3,1), .., M(n, 1)
        table[0][1] = 0
        table[i][1] = table[i - 1][1] + array[i]

    # Now iterate for each row until the end
    # For each element calculate M(n, k) = min<1, n - 1>( max( M(i, k - 1), sum<j = i + 1, n> sj ) )
    # Calculate minimum from maximums of either k - 1 partitions or sum of all elements from i + 1 to n
    for row in range(2, n):
        # Iterate for each column where k > 2 until k == num_partitions
        for col in range(2, k + 1):
            max_list = []

            # calculate maximums for n = row and k = col
            for i in range(1, row):
                max_list.append(
                    max(table[i][col - 1], sum(array[i + 1:row + 1]))
                )

            min_value = min(max_list)
            min_value_idx = max_list.index(min_value) + 1  # + 1 since we index from 1 instead of 0
            table[row][col] = min_value
            path[row][col] = min_value_idx

    # Print resulting table
    for row in table:
        print(row)

    print()
    # Print path table
    for row in path:
        print(row)

    # Create the result
    def recounstruct_partition(array, path, n, k):
        if k == 1:
            return array[1:n + 1]  # array has extra None element

        else:
            result = recounstruct_partition(array, path, path[n][k], k - 1)
            # results will be concatenated to a single list and separated by None elements
            return result + [None] + array[path[n][k]:n]

    return recounstruct_partition(array, path, len(array) - 1, num_partitions)


print(linear_partition_problem([100, 100, 100], 3))
