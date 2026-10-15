class Expression:
    pass

class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value

class AdditionExpression(Expression):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

class ExpressionPrinter:
    @staticmethod
    def print(expr, buffer):
        if isinstance(expr, DoubleExpression):
            buffer.append(str(expr.value))
        elif isinstance(expr, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(expr.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(expr.right, buffer)
            buffer.append(")")

Expression.print = lambda self, b: ExpressionPrinter.print(self, b)


if __name__ == "__main__":
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        ))
    buffer = []
    e.print(buffer)
    print("".join(buffer))