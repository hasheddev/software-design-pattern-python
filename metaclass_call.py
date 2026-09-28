class MyMeta(type):
    def __call__(cls, *args, **kwargs):
        print("1. Intercepted call in Metaclass")
        
        # This delegates to type.__call__, which orchestrates __new__ and __init__
        instance = super().__call__(*args, **kwargs) 
        
        print("4. Back in Metaclass after initialization")
        return instance

class MyClass(metaclass=MyMeta):
    def __new__(cls, *args, **kwargs):
        print("2. MyClass.__new__ executed")
        return super().__new__(cls)

    def __init__(self):
        print("3. MyClass.__init__ executed")

# Trigger the chain
obj = MyClass()
