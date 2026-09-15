class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__code = Code(root_name)

    def add_field(self, type, name):
        self.__code.fields.append(Attribute(type, name))
        return self

    def __str__(self):
        return str(self.__code)

class Code:
    def __init__(self, name):
        self.name = name
        self.fields = []
     
    def __str__(self):
        lines = [f"class {self.name}:"]
        if len(self.fields) == 0:
            lines.append("  pass")
        else:
            lines.append("  def __init__(self):")
            for field in self.fields:
                lines.append(str(field))
        return "\n".join(lines)
    
    
class Attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __str__(self):
        return f"    self.{self.name} = {self.value}"