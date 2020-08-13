def computeBoxAveraging3x3(pixel_array, image_width, image_height):
    new_array = [[0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0]]

    for row_pos, row in enumerate(pixel_array, start=0):
        for position, pixel in enumerate(row, start=0):
            if row_pos == 0 or row_pos == image_height - 1:
                new_array[row_pos][position] = 0.0
            elif position == 0 or position == image_width - 1:
                new_array[row_pos][position] = 0.0
            else:
                new_array[row_pos][position] = calculation(position, row, pixel_array)
    return new_array

def calculation(pos, r, p_a):
    # pos: position of current pixel in row
    # r: row
    # p_a = pixel array
    left = p_a[p_a.index(r) - 1][pos - 1] + p_a[p_a.index(r)][pos - 1] + p_a[p_a.index(r) + 1][pos - 1]
    middle = p_a[p_a.index(r) - 1][pos] + p_a[p_a.index(r)][pos] + p_a[p_a.index(r) + 1][pos]
    right = p_a[p_a.index(r) - 1][pos + 1] + p_a[p_a.index(r)][pos + 1] + p_a[p_a.index(r) + 1][pos + 1]
    number = abs((left + middle + right) / 9)
    return number