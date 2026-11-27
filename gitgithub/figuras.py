"""Modulo para el calculo de areas de figuras geometricas.
Version refactorizada: nombres claros y una funcion por figura.
"""


def area_rectangulo(base: float, altura: float) -> float:
    # Area de un rectangulo = base multiplicada por la altura
    return base * altura


def area_triangulo(base: float, altura: float) -> float:
    # Area de un triangulo = (base por altura) dividido entre 2
    return (base * altura) / 2


def area_circulo(radio: float) -> float:
    # Area de un circulo = pi multiplicado por el radio al cuadrado
    import math
    return math.pi * radio ** 2
