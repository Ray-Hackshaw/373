def computeVerticalEdgesSobelAbsolute(pixel_array, image_width, image_height):
    new_array = [[0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0]]

    for row_pos, row in enumerate(pixel_array, start=0):
        for position, pixel in enumerate(row, start=0):
            val = 0.000
            if row_pos == 0 or row_pos == image_height - 1:
                new_array[row_pos][position] = 0.0
            elif position == 0 or position == image_width - 1:
                new_array[row_pos][position] = 0.0
            else:
                new_array[row_pos][position] = calculation(position, row, pixel_array)
    return new_array

def calculation(pos, r, p_a):
    tl = -1 * p_a[p_a.index(r) - 1][pos - 1]
    ml = -2 * p_a[p_a.index(r)][pos - 1]
    bl = -1 * p_a[p_a.index(r) + 1][pos - 1]
    left_col = tl + ml + bl
    tr = 1 * p_a[p_a.index(r) - 1][pos + 1]
    mr = 2 * p_a[p_a.index(r)][pos + 1]
    br = 1 * p_a[p_a.index(r) + 1][pos + 1]
    right_col = tr + mr + br
    number = abs((left_col + right_col) / 8)
    return number