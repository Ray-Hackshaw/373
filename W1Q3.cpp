bool coplanar(Vector3 p, Vector3 q, Vector3 r, Vector3 s) {
    Vector3 v1 = Vector3(q.x - p.x, q.y - p.y, q.z - p.z);
    Vector3 v2 = Vector3(r.x - q.x, r.y - q.y, r.z - q.z);
    Vector3 v3 = Vector3(s.x - r.x, s.y - r.y, s.z - r.z);
    
    Vector3 cproduct = cross(v1, v2);
    double dproduct = dot(cproduct, v3);
    
    
    if (dproduct == 0) {
        return true;
    }
    else {
        return false;
    }
}