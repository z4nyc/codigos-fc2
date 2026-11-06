
def simpson(f, a, b, h, *args):
    """
    Obtiene la integral numérica de la función f por medio de la regla
    de Simpson
    -----------------
    f: Función integrando
    a, b: Límites de integración
    """
    x = np.arange(a, b, 2*h)
    return (h/3)*np.sum(f(x, *args) + 4*f((x+h), *args) + f(x + 2*h, *args))
