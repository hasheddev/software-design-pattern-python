from enum import Enum, auto
from typing import Optional, Union

class Token:
    class Type(Enum):
       INTEGER = auto() 
       PLUS = auto()
       MINUS = auto()
       LPAREN = auto()
       RPAREN = auto()

    def __init__(self, text: str, type: "Token.Type") -> None:
        self.text = text
        self.type = type

    def __str__(self) -> str:
        return f"`{self.text}`"

def lex(input: str):
    result:list[Token] = []
    i = 0
    input_len = len(input)
    while i < input_len:
        char = input[i]
        if char == '+':
            result.append(Token("+", Token.Type.PLUS))
            i += 1
        elif char == '-':
            result.append(Token("-", Token.Type.MINUS))
            i += 1
        elif char == '(':
            result.append(Token("(", Token.Type.LPAREN))
            i += 1
        elif char == ')':
            result.append(Token(")", Token.Type.RPAREN))
            i += 1
        elif char == '+':
            result.append(Token("+", Token.Type.PLUS))
            i += 1
        elif char.isdigit():
            j = i
            while j < input_len and input[j].isdigit():
                j += 1
            
            number_str = input[i:j]
            result.append(Token(number_str, Token.Type.INTEGER))
            i = j
        else:
           i += 1
    return result


class Integer:
    def __init__(self, value) -> None:
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


def parse(tokens: list[Token]):
    result = BinaryExpression()
    has_lhs = False
    i = 0
    token_len = len(tokens)
    while i < token_len:
        token = tokens[i]
        if token.type == Token.Type.INTEGER:
            value = Integer(int(token.text))
            if not has_lhs:
                result.left = value
                has_lhs =  True
            else:
                result.right = value
        elif token.type == Token.Type.PLUS:
            result.type = BinaryExpression.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:
            j = i
            while j  < token_len:
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i + 1: j]
            element = parse(subexpression)
            if not has_lhs:
                result.left = element
                has_lhs = True
            else:
                result.right = element
            i = j
        i += 1
    return result



def calc(input: str):
    tokens = lex(input)
    print(" ".join(map(str, tokens)))
    parsed = parse(tokens)
    print(f"{input} = {parsed.value}")

if __name__ == "__main__":
    calc("(13+4)-(12+1)")