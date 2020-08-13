Colour complement(Colour c) {
    Colour x = Colour(1.0 - c.r, 1.0 - c.g, 1.0 - c.b);
    return x;
}