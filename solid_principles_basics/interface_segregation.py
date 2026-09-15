#Provide only necessary methods in an interface

class Machine:
    def print(self, doc):
        raise NotImplementedError()
    def fax(self, doc):
        raise NotImplementedError()
    def scan(self, doc):
        raise NotImplementedError()

class MultiFunctionPrinter(Machine):
    def print(self, doc):
        pass
    def fax(self, doc):
        pass
    def scan(self, doc):
        pass

class OldFAshionedPrinter(Machine):#cannot fax and scan
    def print(self, doc):
        pass
    #user might call fax but get no result or we migt throw an error
    def fax(self, doc):
        pass
    def scan(self, doc):
        pass

#Keep things granular

class Printer:
    def print(self, doc):
        raise NotImplementedError()

class Scanner:
    def scan(self, doc):
        raise NotImplementedError()

class Fax:
    def fax(self, doc):
        raise NotImplementedError()

class Photocopier(Printer, Scanner):
    def print(self, doc):
        pass
    def scan(self, doc):
        pass