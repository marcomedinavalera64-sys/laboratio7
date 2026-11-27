def area_rectangulo(base: float, altura: float) -> float:
    return base * altura


def area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2


def area_circulo(radio: float) -> float:
    import math
    return math.pi * radio ** 2
