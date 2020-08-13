def scaleTo0And255AndQuantize(pixel_array, image_width, image_height):
    min_max = computeMinAndMaxValues(pixel_array, image_width, image_height)
    smaller, bigger = min_max[0], min_max[1]
    mult = 0
    if (bigger - smaller) > 0:
        mult = 255/(bigger - smaller)
    first, second = [], []

    for item in pixel_array[0]:
        if mult <= 0:
            first.append(0)
        else:
            first.append(round(mult * (item - smaller)))
    for item in pixel_array[1]:
        if mult <= 0:
            second.append(round(mult * (item - smaller)))
        else:
            second.append(round(mult * (item - smaller)))
    return [first, second]