import inspect


def introspection(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [],
        'methods': [],
        'module': inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else '__main__'
    }

    for attribute_name in dir(obj):
        attribute = getattr(obj, attribute_name)
        if callable(attribute):
            info['methods'].append(attribute_name)
        else:
            info['attributes'].append(attribute_name)

    return info


class Example:
    def __init__(self):
        self.attr1 = 'str'
        self.attr2 = 123

    def method1(self):
        pass

    def method2(self):
        pass


number_info = introspection(13)
print(number_info)

list_info = introspection(['asd', 123, [1, 2], False])
print(list_info)

example_obj = Example()
example_info = introspection(example_obj)
print(example_info)
