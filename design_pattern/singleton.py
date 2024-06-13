class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True

# Usage
singleton1 = Singleton(10)
singleton2 = Singleton(20)

print(singleton1 is singleton2)  # Output: True
print(singleton1.value)          # Output: 10
print(singleton2.value)          # Output: 10
