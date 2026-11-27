from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def nombre(self) -> str:
        ...


class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def nombre(self) -> str:
        return "Rectangulo"


class Triangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return (self.base * self.altura) / 2

    def nombre(self) -> str:
        return "Triangulo"


class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def nombre(self) -> str:
        return "Circulo"

class Trapecio(Figura):
    def __init__(self, base_mayor: float, base_menor: float, altura: float):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def area(self) -> float:
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def nombre(self) -> str:
        return "Trapecio"


class GeneradorReporte:


    @staticmethod
    def imprimir(figuras: list[Figura]) -> None:
        for figura in figuras:
            print(f"Area de {figura.nombre()}: {figura.area():.2f}")


if __name__ == "__main__":
    figuras = [
        Rectangulo(4, 5),
        Triangulo(6, 3),
        Circulo(2),
        Trapecio(8, 4, 3), 
    ]
    GeneradorReporte.imprimir(figuras)
