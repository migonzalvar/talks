#!/usr/bin/env python3

import datetime
from decimal import Decimal
from inspect import Signature, Parameter
import json


class Field:
    def __init__(self, key):
        self.key = key

    def from_json(self, value):
        return value

    def to_json(self, value):
        return value


class DateField(Field):
    def from_json(self, value):
        return datetime.datetime.strptime(value, '%d/%m/%Y').date()

    def to_json(self, value):
        return value.strftime('%d/%m/%Y')


class DecimalField(Field):
    def from_json(self, value):
        return Decimal(str(value))

    def to_json(self, value):
        return float(value)


class ModelMeta(type):
    def __new__(mcs, clsname, bases, clsdict):
        fields = {}
        newdict = {}
        params = []
        for name, value in clsdict.items():
            if isinstance(value, Field):
                # Uno de los nuestros
                fields[name] = value
                params.append(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD, default=None))

            newdict[name] = value

        newdict['fields'] = fields
        newdict['__signature__'] = Signature(params)

        return type.__new__(mcs, clsname, bases, newdict)


class Base(metaclass=ModelMeta):
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
        d = {}
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
    start_date = DateField('iniFecha')
    amount = DecimalField('imp')
    name = Field('nombre')



def test_model():
    s = '{"iniFecha": "12/05/2010", "imp": 12.24, "nombre": "Don Pimp\xf3n"}'

    obj = Model.from_json(s)

    assert json.loads(obj.to_json()) == json.loads(s)

    assert obj.name == 'Don Pimpón'
    assert obj.start_date == datetime.date(2010, 5, 12)
    assert obj.amount == Decimal('12.24')
    assert repr(obj) == "Model(amount=Decimal('12.24'), start_date=datetime.date(2010, 5, 12), name='Don Pimpón')"
