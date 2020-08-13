double dot(Vector3 u, Vector3 v) {
    double first = (u.x * v.x);
    double second = (u.y * v.y);
    double third = (u.z * v.z);
    double dotproduct = first + second + third;
    return dotproduct;
}