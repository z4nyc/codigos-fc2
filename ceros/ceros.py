import numpy as np

def bis(f, a, b, tol = 1e-6):
    """
    Método de la bisección
    ----------------------
    f: Función de la cual queremos encontrar raices (f(x) = 0)
    a: Extremo izquierdo del intervalo inicial de busqueda
    b: Extremo derecho del intervalo inicial de busqueda
    tol: Mínimo error aceptado para el valor de la raíz encontrado
    """
    err = (b-a)/2
    while(err > tol):
        c = (a + b)/2
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        err = np.abs(b-a)/2
    return c

def regfal(f, a, b, tol = 1e-6):
    """
    Método de falsa posición (regula falsi)
    ---------------------------------------
    f: Función de la cual queremos enocntrar raices
    a: Extremo izquierod del intervalo de busqueda
    b: Extremo derecho del intervalo inicial de busqueda
    """
    err = np.abs(b-a)/2
    while(err > tol):
        err = f(b)*(b - a)/(f(b) - f(a)) #Aquí definimos err = b-c
        b = b - err
    return b

def newra(f, df, x0, tol = 1e-6):
    """
    Método de Newton-Raphson
    ------------------------
    f: Función a resolver
    df: Derivada de la función a resolver
    x0: Valor inicial (semilla) para la busqueda
    """
    stop = False
    while(not stop):
        h = -f(x0)/df(x0)
        x0 = x0 + h
        stop = np.abs(h) < tol or np.abs(f(x0)) < tol

    return x0

def secante(f, x0, x1, tol = 1e-6):
    """
    Método de la secante
    --------------------
    f: Función a resolver
    x0, x1: Valores inciales (semilla) para la busqueda
    """
    stop = False
    while(not stop):
        h = f(x0)*(x1 - x0)/(f(x1) - f(x0))
        x0, x1 = x1, x0 -h
        stop = np.abs(h) < tol or np.abs(f(x0)) < tol

    return x0
