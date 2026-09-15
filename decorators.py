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
#class decorator  do not work with classmethods and staticmethods
