def calculation(g):
    r, g, b = g[0], g[1], g[2]
    red = (0.299*r)
    green = (0.587*g)
    blue = (0.114*b)
    return round(red + green + blue)

def computeRGBToGreyscale(pixel_array_r, pixel_array_g, pixel_array_b, image_width, image_height):
    g, first, second = [], [], []
    for i in range(0, 3):
        while len(g) != 3:
            g.append(pixel_array_r[0][i])
            g.append(pixel_array_g[0][i])
            g.append(pixel_array_b[0][i])
        first.append(calculation(g))
        g = []
    for i in range(0, 3):
        while len(g) != 3:
            g.append(pixel_array_r[1][i])
            g.append(pixel_array_g[1][i])
            g.append(pixel_array_b[1][i])
        second.append(calculation(g))
        g = []
    greyscale_pixel_array = [first, second]
    return greyscale_pixel_array