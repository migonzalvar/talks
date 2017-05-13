"""Demo using a registry with a singleton metaclass."""


class Singleton(type):
    """Using this metaclass ensures only one instance."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Registry(metaclass=Singleton):
    """Classs which allows only one instance and keeps handlers."""

    def __init__(self):
        self.items = {}

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def get(self, key, default=None):
        return self.items.get(key, default)

    def add(self, model, item):
        if item not in self.items:
            self.items[model] = item


def register(model):
    """Decorator to add items to the registry"""
    def _register(item):
        Registry().add(model, item)
        return item
    return _register


class Model:
    pass


@register(Model)
class Handler:
    pass


def test_registry_is_a_singleton():
    registry1 = Registry()
    registry2 = Registry()
    assert registry1 is registry2


def test_register_decorator_is_working():
    registry = Registry()
    handler_class = registry.get(Model)
    assert handler_class is Handler
