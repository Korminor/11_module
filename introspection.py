from inspect import getmodule
from pprint import pprint

def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': obj.__dir__,
        'methods': dir(obj),
        'module': getmodule(obj)
    }
class MyClass:
    pass
obj = MyClass()
number_info = introspection_info(42)
pprint(number_info)