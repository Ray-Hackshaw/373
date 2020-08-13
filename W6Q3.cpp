double Sphere::Intersect(Vector source, Vector d)
{   
    
    source = (source - translation) / scaling;
    d = d/scaling;
	
	float A = d.Dot(d);
	float B = 2 * (source.Dot(d));
	float C = (source.Dot(source)) - 1;
	float t = -1.0;
	float det = (B*B) - (4*A*C);
    float t1 = (-B + (sqrt(det))) / (2*A);
	float t2 = (-B - (sqrt(det))) / (2*A);
	
	if(t1 < t2 && t1 > 0){
        return t1;
    }
    else if(t2 < t1 && t2 > 0) {
        return t2;
    }
    else {
        return t;
    }
}

Vector Sphere::Normal(Vector p)
{   
    Vector s1 = (p - translation) / scaling;
    Vector s2 = s1 / scaling;
    s2 = s2.Normalize();
	return s2;
}