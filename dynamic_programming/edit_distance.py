def edit_distance(string_a, string_b) -> int:
    rows, cols = len(string_a) + 1, len(string_b) + 1

    table = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        table[row][0] = row
    for col in range(cols):
        table[0][col] = col

    for row in range(1, rows):
        for col in range(1, cols):
            if string_a[row - 1] == string_b[col - 1]:
                table[row][col] = table[row - 1][col - 1]
            else:
                table[row][col] = min(table[row - 1][col], table[row][col - 1], table[row - 1][col - 1]) + 1

    for row in table: print(row)

    return table[rows - 1][cols - 1]


print(edit_distance("kelm", "hello"))
