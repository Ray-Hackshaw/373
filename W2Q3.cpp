#include <iostream>
using namespace std;

void drawMesh(Vector3 vertices[], Vector3 colors[], int indices[], int numIndices){
    glBegin(GL_TRIANGLES);

    for (int i = 0; i < numIndices; i++){
        int nx = indices[i];
        CRColor3d(colors[nx].x, colors[nx].y, colors[nx].z);
        CRVertex3d(vertices[nx].x, vertices[nx].y, vertices[nx].z);
    }

    glEnd();
}