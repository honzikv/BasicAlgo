def longest_common_subsequence(string_a, string_b):
    rows, cols = len(string_a) + 1, len(string_b) + 1

    # Create a n x m table, where n is the length of string_a + 1 and m is the length of string_b + 1
    table = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            if string_a[row - 1] == string_b[col - 1]:
                table[row][col] = table[row - 1][col - 1] + 1
            else:
                table[row][col] = max(table[row - 1][col], table[row][col - 1])

    common_subseq_len = table[rows - 1][cols - 1]

    # construct subsequence, this is an overhead and could be implemented in the for loop before this one
    subseq = {}
    for row in range(1, rows):
        for col in range(1, cols):
            if string_a[row - 1] == string_b[col - 1] and table[row][col] not in subseq:
                subseq[table[row][col]] = string_a[row - 1]

    result_subseq = ''
    for i in range(1, common_subseq_len + 1):
        result_subseq += subseq[i]

    return result_subseq, common_subseq_len


print(longest_common_subsequence('computer', 'houseboat'))
