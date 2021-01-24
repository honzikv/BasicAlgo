from typing import Tuple


def longest_common_substring(string_a: str, string_b: str):
    rows, cols = len(string_a) + 1, len(string_b) + 1
    # Create a n x m table, where n is the length of string_a + 1 and m is the length of string_b + 1
    table = [[0 for _ in range(rows)] for _ in range(cols)]

    start_end_idx_pair = (None, None)  # start and end indexes of the substring
    common_substr_len = 0
    for row in range(1, rows):
        for col in range(1, cols):
            if string_a[row - 1] != string_b[col - 1]:
                table[row][col] = 0
            else:
                table[row][col] = table[row - 1][col - 1] + 1
                if table[row][col] > common_substr_len:
                    common_substr_len = table[row][col]
                    start_end_idx_pair = (row, col)

    if start_end_idx_pair == (None, None):
        return "", 0
    print(start_end_idx_pair)

    if start_end_idx_pair[0] > start_end_idx_pair[1]:
        return string_a[start_end_idx_pair[1]:start_end_idx_pair[0]], common_substr_len
    return string_b[start_end_idx_pair[0]:start_end_idx_pair[1]], common_substr_len


print(longest_common_substring('hello', 'aloha'))
