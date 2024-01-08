class NoDunderAttributes(type):
    def __new__(cls, name, bases, attrs):
        for atr in attrs:
            if atr.startswith(f'_{name}__'):
                raise ValueError('Cannot have attribute names starting with "__"')
        return super().__new__(cls, name, bases, attrs)


class MyPrivateClass(metaclass=NoDunderAttributes):
    __secret_attribute = 10