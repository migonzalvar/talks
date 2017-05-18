% Mira mamá, sin ifs
% Miguel González
% 2017-05-18

# Disclaimer

## Ejemplo a título demostrativo

# Problema

## Muchos if

![ifs](./everywhere.jpg){width=70%}

## Porque...

¡Python no tiene `switch`!

## Clásico

```python
def fn(edad):
    if edad <= 12:
        return 'Minibasket'
    elif 12 < x <= 14:
        return 'Infantil'
    elif 14 < x <= 16:
        return 'Cadete'
    elif 16 < x <= 18:
        return 'Junior'
    elif 18 < x:
        return 'Absoluta'
    else:
        return 'N/A'
```

## Tabla

```python
TABLA = (
    (lambda x: x <= 12, 'Minibasket'),
    (lambda x: 12 < x <= 14, 'Infantil'),
    (lambda x: 14 < x <= 16, 'Cadete'),
    (lambda x: 16 < x <= 18, 'Junior'),
    (lambda x: 18 < x, 'Absoluta'),
    (lambda x: True, 'N/A'),
)

def fn(edad):
    for check, categoria in TABLA:
        if check(edad):
            return edad
```

## Tabla... ¿de verdad?

- Lambdas?
- Un poco cutre Python, ¡puedes hacerlo mejor!

## Decoradores

```python
TABLA2 = []

def register(resultado):
    global TABLA2
    def _register(check):
        TABLA2.append([check, resultado])
        return check
    return _register
```

----

```python
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
```

----

```python
def fn3(edad):
    for check, categoria in TABLA2:
        if check(edad):
            return categoria    
```

**fn2 y fn3 son iguales**