from copy import deepcopy

class Token:
    def __init__(self, value=0):
        self.value = value
    

class Momento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []


    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        return Momento(deepcopy(self.tokens))

    def revert(self, momento):
        self.tokens = [Token(x.value) for x in momento]