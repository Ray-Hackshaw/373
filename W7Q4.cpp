CVec3df c(float t){ 
     if (t >= 0 && t <= 0.5) {
         return CVec3df(2*t, 0, 2 + (2*t));
     } else {
         return CVec3df(1 + 2*(cos((t*Pi)-Pi)), 0, 1 + 2*sin(t*Pi));
     }
}