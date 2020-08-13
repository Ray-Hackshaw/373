def computeStrongVerticalEdgesBySubtractingHorizontal(vertical_edges, horizontal_edges, image_width, image_height):
    new_array = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]

    for row_pos, row in enumerate(vertical_edges, start=0):
        for position, pixel in enumerate(row, start=0):
            num = vertical_edges[row_pos][position] - horizontal_edges[row_pos][position]
            if num <= 0:
                new_array[row_pos][position] = 0
            else:
                new_array[row_pos][position] = num
    return new_array