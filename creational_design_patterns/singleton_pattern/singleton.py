#custom alocator
class Database:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    #initializer gets called twoce
    print(d1 == d2)