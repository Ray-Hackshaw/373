def computeThresholdGE(pixel_array, threshold_value, image_width, image_height):
    new_array = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]

    for row_pos, row in enumerate(pixel_array, start=0):
        for position, pixel in enumerate(row, start=0):
            num = pixel_array[row_pos][position]
            if num < threshold_value:
                new_array[row_pos][position] = 0
            else:
                new_array[row_pos][position] = 255
    return new_array