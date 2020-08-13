CVec3df c(float t, CVec3df p1, CVec3df p4, CVec3df r1, CVec3df r4)
{   
    CVec3df p = (t*t*(2*t-3)+1)*p1 + ((-2*t+3)*t*t)*p4 + t*(t*(t-2)+1)*r1 + t*t*(t-1)*r4;  
    return p; 
}