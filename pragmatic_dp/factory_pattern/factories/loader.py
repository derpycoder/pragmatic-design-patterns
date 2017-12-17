from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .ifactory import IFactory

def load_factory(factory_name):
    try:
        factory_module = import_module(f'.{factory_name}', 'factories')
    except ImportError:
        factory_module = import_module(f'.null_factory', 'factories')

    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m))

    for name, _class in classes:
        if issubclass(_class, IFactory):
            return _class()