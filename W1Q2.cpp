Vector3 lerp(Vector3 u, Vector3 v, double t) {
    u.x = u.x * (1-t);
    u.y = u.y * (1-t);
    u.z = u.z * (1-t);
    Vector3 a = Vector3(u.x, u.y, u.z);
    v.x = v.x * t;
    v.y = v.y * t;
    v.z = v.z * t;
    Vector3 b = Vector3(v.x, v.y, v.z);
    Vector3 c = Vector3(u.x + v.x, u.y + v.y, u.z + v.z);
    return c;
}