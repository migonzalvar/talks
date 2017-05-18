import pytest

# Clásico

def fn1(edad):
    if edad <= 12:
        return 'Minibasket'
    elif 12 < edad <= 14:
        return 'Infantil'
    elif 14 < edad <= 16:
        return 'Cadete'
    elif 16 < edad <= 18:
        return 'Junior'
    elif 18 < edad:
        return 'Absoluta'
    else:
        return 'N/A'

# Tabla

TABLA = (
    (lambda x: x <= 12, 'Minibasket'),
    (lambda x: 12 < x <= 14, 'Infantil'),
    (lambda x: 14 < x <= 16, 'Cadete'),
    (lambda x: 16 < x <= 18, 'Junior'),
    (lambda x: 18 < x, 'Absoluta'),
    (lambda x: True, 'N/A'),
)

def fn2(edad):
    for check, categoria in TABLA:
        if check(edad):
            return categoria

# Decoradores

TABLA2 = []


def register(resultado):
    global TABLA2
    def _register(check):
        TABLA2.append([check, resultado])
        return check
    return _register


@register('Minibasket')
def _(edad):
    return edad <= 12


@register('Infantil')
def _(edad):
    return 12 < edad <= 14


@register('Cadete')
def _(edad):
    return 14 < edad <= 16


@register('Junior')
def _(edad):
    return 16 < edad <= 18


@register('Absoluta')
def _(edad):
    return 18 < edad


@register('N/A')
def _(edad):
    return True


def fn3(edad):
    for check, categoria in TABLA2:
        if check(edad):
            return categoria    

# Test

@pytest.mark.parametrize('edad', [
    0, 1, 12, 13, 15, 18, 20, -1
])
def test(edad):
    assert fn1(edad) == fn2(edad) == fn3(edad), edad
