def dec_a(func):
    print("Executing dec_a setup")
    def wrapper():
        print("-> Entering dec_a wrapper")
        func()
        print("<- Exiting dec_a wrapper")
    return wrapper

def dec_b(func):
    print("Executing dec_b setup")
    def wrapper():
        print("  -> Entering dec_b wrapper")
        func()
        print("  <- Exiting dec_b wrapper")
    return wrapper

# Decorators applied here:
@dec_a
@dec_b
def greet():
    print("    *** Running greet() ***")

print("\n--- Definition Complete, Now Calling Function ---\n")
greet()

def ngreet():
    print("    *** Running greet() ***")

print('\n\n')
print("---------")
print("Equivalent")
print("---------")
ngreet = dec_a(dec_b(ngreet))

ngreet()

def debugmethods(cls) :
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, dec_a(val))
    return cls
#class decorator  do not work with classmethods and staticmethods

def log_all_methods(cls):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):
            # Wrap the original method
            def make_wrapper(method):
                def wrapper(*args, **kwargs):
                    print(f"Calling method: {method.__name__}")
                    return method(*args, **kwargs)
                return wrapper
            
            setattr(cls, attr_name, make_wrapper(attr_value))
    return cls

@log_all_methods
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 3)) 
# Output:
# Calling method: add
# 8

