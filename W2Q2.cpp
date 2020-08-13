void drawTriangleTile(Vector3 verticesTriangles[]) {
    glBegin(GL_TRIANGLES);
    CRColor3d(1.0, 0.5, 0.0);
    
    CRVertex3d(verticesTriangles[2].x, verticesTriangles[2].y, verticesTriangles[2].z);  
    CRVertex3d(verticesTriangles[0].x, verticesTriangles[0].y, verticesTriangles[0].z);
    CRVertex3d(verticesTriangles[1].x, verticesTriangles[1].y, verticesTriangles[1].z);
    
    CRColor3d(0.0, 0.0, 1.0);
    
    CRVertex3d(verticesTriangles[2].x, verticesTriangles[2].y, verticesTriangles[2].z);
    CRVertex3d(verticesTriangles[1].x, verticesTriangles[1].y, verticesTriangles[1].z);
    CRVertex3d(verticesTriangles[3].x, verticesTriangles[3].y, verticesTriangles[3].z);
    
    CRVertex3d(verticesTriangles[2].x, verticesTriangles[2].y, verticesTriangles[2].z);
    CRVertex3d(verticesTriangles[3].x, verticesTriangles[3].y, verticesTriangles[3].z);
    CRVertex3d(verticesTriangles[4].x, verticesTriangles[4].y, verticesTriangles[4].z);
    
    CRVertex3d(verticesTriangles[2].x, verticesTriangles[2].y, verticesTriangles[2].z);
    CRVertex3d(verticesTriangles[4].x, verticesTriangles[4].y, verticesTriangles[4].z);
    CRVertex3d(verticesTriangles[0].x, verticesTriangles[0].y, verticesTriangles[0].z);
    glEnd();
}