def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    if numero in (2, 3):
        return True
    if numero % 2 == 0:
        return False
    limite = int(numero ** 0.5) + 1
    for divisor in range(3, limite, 2):
        if numero % divisor == 0:
            return False
    return True
