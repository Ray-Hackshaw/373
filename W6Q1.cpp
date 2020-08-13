for(int r=0; r<windowHeight; r++) {
  for(int c=0; c<windowWidth; c++) {
    dx = -n.x*N + W * ((float(2 * c) / float((windowWidth - 1)) - 1)) * u.x + H * v.x * ((float(2 * r) / float((windowHeight - 1)) - 1));
    dy = -n.y*N + W * ((float(2 * c) / float((windowWidth - 1)) - 1)) * u.y + H * v.y * ((float(2 * r) / float((windowHeight - 1)) - 1));
    dz = -n.z*N + W * ((float(2 * c) / float((windowWidth - 1)) - 1)) * u.z + H * v.z * ((float(2 * r) / float((windowHeight - 1)) - 1));

    Vector d = Vector(dx, dy, dz);
    Hit hit = intersect(eye, d);

    Color color = shade(hit);
    glColor3f(color.r, color.g, color.b);
    glVertex2f((GLfloat)c, (GLfloat)r);

  }

}