Vector2 coordinates(CIEColour c) {
    Vector2 V = Vector2(c.X / (c.X + c.Y + c.Z), c.Y / (c.X + c.Y + c.Z));
    return V;
}