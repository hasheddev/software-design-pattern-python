
# Interpreter Coding Exercise
# You are asked to write an expression processor for simple numeric expressions with the following constraints:

# Expressions use integral values (e.g., '13' ), single-letter variables defined in Variables, as well as + and - operators only

# There is no need to support braces or any other operations

# If a variable is not found in variables  (or if we encounter a variable with >1 letter, e.g. ab), the evaluator returns 0 (zero)

# In case of any parsing failure, evaluator returns 0

# Example:

# calculate("1+2+3")  should return 6

# calculate("1+2+xy")  should return 0

# calculate("10-2-x")  when x=3 is in variables  should return 5
from enum import Enum, auto
from typing import Optional, Union


class Token:
    class Type(Enum):
       INTEGER = auto() 
       PLUS = auto()
       MINUS = auto()

    def __init__(self, text: str, type: "Token.Type") -> None:
        self.text = text
        self.type = type

    def __str__(self) -> str:
        return f"`{self.text}`"


class Integer:
    def __init__(self, value: int) -> None:
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()
    
    def __init__(self) -> None:
        self.type: Optional[BinaryExpression.Type] = None
        self.left: Optional[Union[Integer, "BinaryExpression"]] = None
        self.right: Optional[Union[Integer, "BinaryExpression"]] = None

    @property
    def value(self) -> int:
        if self.left is None or self.right is None:
            raise ValueError("Expression is incomplete")       
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value
        return 0

class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression: str):
        try:
            tokens = self.lex(expression)
            if tokens is None or len(tokens) == 0:
                return 0
            return self.parse(tokens)
        except Exception:
            return 0

    def lex(self, token_str: str) -> list[Token] | None:
        str_len = len(token_str)
        result: list[Token] = []
        i = 0        
        while i < str_len:
            char = token_str[i]
            if char == "+":
                result.append(Token(char, Token.Type.PLUS))
                i += 1
            elif char == "-":
                result.append(Token(char, Token.Type.MINUS))
                i += 1
            elif char.isdigit():
                j = i
                while j < str_len and token_str[j].isdigit():
                    j += 1
                number_str = token_str[i:j]
                result.append(Token(number_str, Token.Type.INTEGER))
                i = j
            elif char.isalpha():
                j = i
                while j < str_len and token_str[j].isalpha():
                    j += 1
                
                var_name = token_str[i:j]
                if len(var_name) > 1:
                    return None

                if var_name not in self.variables:
                    return None
                var_value = self.variables[var_name]
                result.append(Token(str(var_value), Token.Type.INTEGER))
                i = j
            else:
                i += 1

        return result

    def parse(self, tokens: list[Token]) -> int:
    
        if len(tokens) == 0:
            return 0

        if len(tokens) == 1:
            if tokens[0].type == Token.Type.INTEGER:
                return int(tokens[0].text)
            return 0
        
        expression = BinaryExpression()
        token_len = len(tokens)
        i = 0
        while i < token_len:
            token = tokens[i]
            if token.type == Token.Type.INTEGER:
                value = Integer(int(token.text))
                if expression.left is None:
                    expression.left = value
                elif expression.right is None:
                    expression.right = value
                else:
                    new_expression = BinaryExpression()
                    new_expression.left = expression
                    token = tokens[i - 1]
                    if token.type in [Token.Type.PLUS, Token.Type.MINUS]:
                        new_expression.type = BinaryExpression.Type.ADDITION if Token.Type.PLUS else BinaryExpression.Type.SUBTRACTION
                    else:
                        return 0
                    new_expression.right = value
                    expression = new_expression
            elif token.type == Token.Type.PLUS:
                expression.type = BinaryExpression.Type.ADDITION
            elif token.type == Token.Type.MINUS:
                expression.type = BinaryExpression.Type.SUBTRACTION
            i += 1
        return expression.value
    