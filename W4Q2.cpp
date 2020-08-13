double phongSingleColour(double ambientIntensity, double diffuseIntensity, double specularIntensity,double ambientReflecCoef, double diffuseReflecCoef, double specularReflecCoef,double shininess,double kc, double kl, double kq, Vector3 pointOnSurface, Vector3 surfaceNormal, Vector3 lightPosition, Vector3 viewPoint){
    Vector3 s = lightPosition - pointOnSurface;
    Vector3 m = surfaceNormal;
    Vector3 v = viewPoint - pointOnSurface;
    Vector3 h = s.normalized() + v.normalized();
    
    double alpha = shininess;
    double d = s.magnitude();
    
    double ambient = ambientIntensity * ambientReflecCoef;
    double diffuseFirst = diffuseIntensity * diffuseReflecCoef;
    double specularFirst = specularIntensity * specularReflecCoef;
    
    double diffuse = diffuseFirst * ((dot(s, m))/(d * m.magnitude()));
    double specular = specularFirst * (pow(((dot(h, m))/(h.magnitude() * m.magnitude())), alpha));
    
    double phong = ambient + (diffuse + specular)/(kc + (kl * d) + (kq * (d*d)));
    return phong;
    
    
}