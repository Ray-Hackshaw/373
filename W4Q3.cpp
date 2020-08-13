void drawPixel(int i, int j) 
{
	pointOnSurface = p(i,j);
	Vector3 surfaceNormal = n0 * ((1 - (i/120.0)) * (1 - (j/120.0))) + n1 * (((i/120.0)) * (1 - (j/120.0))) + n2 * ((1 - (i/120.0)) * ((j/120.0))) + n3 * (((i/120.0)) * ((j/120.0))); 
	double c = phongSingleColour(ambientIntensity, diffuseIntensity, specularIntensity,ambientReflecCoef, diffuseReflecCoef, specularReflecCoef, shininess, kc, kl, kq, pointOnSurface, surfaceNormal, lightPosition, viewPoint); 
	glColor3d(c, c, c);
	glVertex3d(pointOnSurface.x, pointOnSurface.y, pointOnSurface.z);
}