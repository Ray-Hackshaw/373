def computeHistogram(pixel_array, image_width, image_height, nr_bins = 256):
    seen = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for row in pixel_array:
        for i in range(0, 8):
            seen[i] = seen[i] + row.count(i)
    return seen