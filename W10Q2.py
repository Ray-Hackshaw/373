from copy import deepcopy

def padding(p_a, width):
    n_a = deepcopy(pixel_array)
    n_a.insert(0, [0 for _ in range(width)])
    n_a.append([0 for _ in range(width)])
    for i in n_a:
        i.insert(0, 0)
        i.append(0)
    return n_a


def computeDilation8Nbh3x3FlatSE(pixel_array, image_width, image_height):
    new_array = [[0 for _ in range(image_width)] for _ in range(image_height)]
    original = deepcopy(pixel_array)
    padded = padding(pixel_array, image_width)
    for row_pos, row in enumerate(original, start=0):
        for position, pixel in enumerate(row, start=0):
            new_array[row_pos][position] = border_calc(position, row_pos, padded)
    return new_array

def border_calc(pos, row_pos, b_p):

    top_left = b_p[row_pos][pos]
    top_middle = b_p[row_pos][pos + 1]
    top_right = b_p[row_pos][pos + 2]

    middle_left = b_p[row_pos + 1][pos]
    middle = b_p[row_pos + 1][pos + 1]
    middle_right = b_p[row_pos + 1][pos + 2]

    bottom_left = b_p[row_pos + 2][pos]
    bottom_middle = b_p[row_pos + 2][pos + 1]
    bottom_right = b_p[row_pos + 2][pos + 2]

    top_row = abs(top_left) + abs(top_middle) + abs(top_right)
    middle_row = abs(middle_left) + abs(middle) + abs(middle_right)
    bottom_row = abs(bottom_left) + abs(bottom_middle) + abs(bottom_right)

    number = 0
    if (top_row + middle_row + bottom_row) != 0:
        number = 1
    return number