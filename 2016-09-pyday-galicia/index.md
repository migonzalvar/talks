
# Mi primera metaclase: un ejemplo práctico

# PyDay Galicia 2016

---

![](img/drink.jpg)


## Metaprogramación


> Escribir programas que escriben o manipulan otros programas (o así mismos)

## Python: metaclases

Controlan la creación de la clases.

## Objetivo

Ejemplo paso a paso de creción de una metaclase para resolver un problema práctico.

# Empezamos

---

![](img/alice.jpg)

## Problema

Una consulta a una API externa me devuelve un JSON feísimo.


```python
s = '''{"iniFecha": "12/05/2010",
        "imp": 12.24,
        "nombre": "Don Pimp\xf3n"}'''
```

- Nombre *camelCase*
- Fecha e suna cadena
- un float para cantidades

---


## Módulo `json`


```python
import json

d = json.loads(s)
d
```




    {'imp': 12.24, 'iniFecha': '12/05/2010', 'nombre': 'Don Pimpón'}



## Deseo

Tener un objeto Python

```python
Model(amount=Decimal('12.24'), start_date=datetime.date(2010, 5, 12), name='Don Pimpón')
```

## 1) Definir modelo


```python
class Model:
    def __init__(self, amount=None, start_date=None, name=None):
        self.amount = amount
        self.start_date = start_date
        self.name = name
        
    def __repr__(self):
        return ('Model('
                'amount={s.amount!r}, '
                'start_date={s.start_date!r}, '
                'name={s.name!r})').format(s=self)
```

## 2) Deserializador


```python
def from_json(s):
    d = json.loads(s)
    obj = Model()
    obj.amount = d['imp']
    obj.start_date = d['iniFecha']
    obj.name = d['nombre']
    return obj

obj = from_json(s)
obj
```




    Model(amount=12.24, start_date='12/05/2010', name='Don Pimpón')



## 3) Serializador


```python
def to_json(obj):
    d = {}
    d['imp'] = obj.amount
    d['iniFecha'] = obj.start_date
    d['nombre'] = obj.name
    return json.dumps(d, indent=2)

d2 = to_json(obj)
print(d2)
```

    {
      "nombre": "Don Pimp\u00f3n",
      "imp": 12.24,
      "iniFecha": "12/05/2010"
    }


## Con tipos nativos!

## Deserializar


```python
from decimal import Decimal as D
import datetime as dt

def from_json(s):
    d = json.loads(s)
    obj = Model()
    obj.amount = D(str(d['imp']))
    obj.start_date = dt.datetime.strptime(d['iniFecha'], '%d/%m/%Y').date()
    obj.name = d['nombre']
    return obj

obj = from_json(s)
obj
```




    Model(amount=Decimal('12.24'), start_date=datetime.date(2010, 5, 12), name='Don Pimpón')



## Serializar


```python
def to_json(obj):
    d = {}
    d['imp'] = str(obj.amount)
    d['iniFecha'] = obj.start_date.strftime('%d/%m/%Y')
    d['nombre'] = obj.name
    return json.dumps(d, indent=2)

d = to_json(obj)
print(d)
```

    {
      "nombre": "Don Pimp\u00f3n",
      "imp": "12.24",
      "iniFecha": "12/05/2010"
    }


## Hasta aqui

Ventajas: más pythonico

- tipos nativos (decimal, fecha)
- atributos en vez de claves

Desventajas: ¡MUCHO CÓDIGO!

- Cada modelo código repetitivo
- Desperdigado


# Metaclases al rescate

---

![](img/chesire.jpg)

## ¿Qué quiero obtener?

```
class Model:
    start_date = DateField('iniFecha')
    amount = DecimalField('imp')
    name = Field('nombre')
    
obj = Model.from_json(s)
```

## Clases por campo


```python
class Field:
    def __init__(self, key):
        self.key = key

    def from_json(self, value):
        return value

    def to_json(self, value):
        return value
```

## Decimal


```python
class DecimalField(Field):
    def from_json(self, value):
        return D(str(value))

    def to_json(self, value):
        return float(value)
```

## Fecha


```python
class DateField(Field):
    def from_json(self, value):
        return dt.datetime.\
            strptime(value, '%d/%m/%Y').date()

    def to_json(self, value):
        return value.strftime('%d/%m/%Y')
```

## Clases

```python
class Meta(type):
    ...

class Base(metaclass=Meta):
    ...

class Model(Base):
    ...
```

## Meta

Es el que intercepta la creación de la clase `Base`.

La clave es el método `__new__`.

En tiempo de ejecución rellenamos `cls.fields`

---

```python
def __new__(mcs, clsname, bases, clsdict):
    fields = collections.OrderedDict()
    for name, value in clsdict.items():
        if isinstance(value, Field):
            fields[name] = value
    clsdict['fields'] = fields
    return type.__new__(mcs, clsname, bases, newdict)
```

---

```
fields = {'amount': <__main__.DecimalField at 0x>,
 'name': <__main__.Field at 0x>,
 'start_date': <__main__.DateField at 0x>}
```

## Base

Implmenta `from_json` (método de clase) y `to_json` (instancia) y `__str__`.

---

```python
class Base(metaclass=Meta):
    @classmethod
    def from_json(cls, s):
        d = json.loads(s)
        obj = cls()
        for field_name, field in cls.fields.items():
            value = field.from_json(d[field.key])
            setattr(obj, field_name, value)
        return obj
```
---

```python
    def to_json(self):
        d = collections.OrderedDict()
        for field_name, field in self.fields.items():
            value = field.to_json(getattr(self, field_name))
            d[field.key] = value
        return json.dumps(d)
```
---
```python
    def __repr__(self):
        class_name = self.__class__.__name__
        payload = []
        for field_name, field in self.fields.items():
            payload.append('{name}={value!r}'.format(name=field_name, value=getattr(self, field_name)))
        payload = ', '.join(payload)
        return '{}({})'.format(class_name, payload)
```

## Model

Nada

```python
class Model(Base):
    amount = DecimalField('imp')
    start_date = DateField('iniFecha')
    name = Field('nombre')
```

## Ejemplo completo


```python
import collections
from inspect import Signature, Parameter

class Meta(type):
    def __new__(mcs, clsname, bases, clsdict):
        fields = collections.OrderedDict()
        params = []
        for name, value in clsdict.items():
            if isinstance(value, Field):
                fields[name] = value
                params.append(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD, default=None))

        clsdict['fields'] = fields
        clsdict['__signature__'] = Signature(params)

        return type.__new__(mcs, clsname, bases, clsdict)

    @classmethod
    def __prepare__(metacls, name, bases):
        return collections.OrderedDict()

class Base(metaclass=Meta):
    __signature__ = None
    fields = None

    @classmethod
    def from_json(cls, s):
        d = json.loads(s)
        obj = cls()
        for field_name, field in cls.fields.items():
            value = field.from_json(d[field.key])
            setattr(obj, field_name, value)
        return obj

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

    def to_json(self):
        d = collections.OrderedDict()
        for field_name, field in self.fields.items():
            value = field.to_json(getattr(self, field_name))
            d[field.key] = value
        return json.dumps(d)

    def __repr__(self):
        class_name = self.__class__.__name__
        payload = []
        for field_name, field in self.fields.items():
            payload.append('{name}={value!r}'.format(name=field_name, value=getattr(self, field_name)))
        payload = ', '.join(payload)
        return '{}({})'.format(class_name, payload)

class Model(Base):
    amount = DecimalField('imp')
    start_date = DateField('iniFecha')
    name = Field('nombre')
```

## Test


```python
# Given
s = '''{"iniFecha": "12/05/2010",
         "imp": 12.24, 
         "nombre": "Don Pimp\xf3n"}'''
```

---


```python
obj = Model.from_json(s)
assert json.loads(obj.to_json()) == json.loads(s)
```

---


```python
obj = Model.from_json(s)
assert obj.name == 'Don Pimpón'
assert obj.start_date == dt.date(2010, 5, 12)
assert obj.amount == D('12.24')
```

---


```python
obj = Model.from_json(s)
assert repr(obj) == (
    "Model(amount=Decimal('12.24'), "
    "start_date=datetime.date(2010, 5, 12), "
    "name='Don Pimpón')"
)
```

# Conclusiones

---

![](img/madhatter.jpg)

## Siguientes pasos

- Campos anidados
- Cambiar firma de `__init__`

## ¿Por qué?

- Fun!
- Declarativo en vez de imperativo
- Reduce código repetitivo

# FIN


## Notas

- Los ORM, formularios... utilizan esta técnica.

- No es necesario hacerlo uno mismos: hay librerías que hacen esto. Ver marshmallow o Django REST framework.

## Más info

- http://chimera.labs.oreilly.com/books/1230000000393
