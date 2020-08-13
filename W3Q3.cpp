SpectralFunction resultantSDF(SpectralFunction light, SpectralFunction surface) {
    SpectralFunction resultant = SpectralFunction(light.r * surface.r, light.g * surface.g, light.b * surface.b);
    return resultant;
}