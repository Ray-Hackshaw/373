def computeErosion8Nbh3x3FlatSE(pixel_array, image_width, image_height):
    new_array = [[0 for _ in range(image_width)] for _ in range(image_height)]
    for row_pos, row in enumerate(pixel_array, start=0):
        for position, pixel in enumerate(row, start=0):
            if row_pos == 0 or row_pos == image_height - 1:
                new_array[row_pos][position] = 0
            elif position == 0 or position == image_width - 1:
                new_array[row_pos][position] = 0
            else:
                new_array[row_pos][position] = border_calc(position, row_pos, pixel_array)
    return new_array

def border_calc(pos, row_pos, p_a):

    top_left = p_a[row_pos - 1][pos - 1]
    top_middle = p_a[row_pos - 1][pos]
    top_right = p_a[row_pos - 1][pos + 1]

    middle_left = p_a[row_pos][pos - 1]
    middle = p_a[row_pos][pos]
    middle_right = p_a[row_pos][pos + 1]

    bottom_left = p_a[row_pos + 1][pos - 1]
    bottom_middle = p_a[row_pos + 1][pos]
    bottom_right = p_a[row_pos + 1][pos + 1]

    top_row = abs(top_left) * abs(top_middle) * abs(top_right)
    middle_row = abs(middle_left) * abs(middle) * abs(middle_right)
    bottom_row = abs(bottom_left) * abs(bottom_middle) * abs(bottom_right)

    number = 0
    if (top_row * middle_row * bottom_row) != 0:
        number = 1
    return number