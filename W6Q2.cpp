double Plane::Intersect(Vector source, Vector d)
{   
    float t = (a - source.Dot(n)) / d.Dot(n);
    if(t > 0) {
        return t;
    }
    else {
        return t = -1.0;
    }
}