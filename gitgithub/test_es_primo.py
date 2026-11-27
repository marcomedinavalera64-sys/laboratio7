from es_primo import es_primo


def test_dos_es_primo():
    assert es_primo(2) is True


def test_cuatro_no_es_primo():
    assert es_primo(4) is False


def test_uno_no_es_primo():
    assert es_primo(1) is False


def test_diecisiete_es_primo():
    assert es_primo(17) is True


def test_numero_negativo_no_es_primo():
    assert es_primo(-5) is False
