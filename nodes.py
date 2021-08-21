from typing import List

from token import Token

class FullExpression:
    def __init__(self, comments: List['Comment'], expression: 'Expression'):
        self.comments = comments
        self.expression = exppression

class Comment:
    def __init__(self, literals: List[Token]):
        self.literals = literals

class Expression:
    def __init__(self, operators: List[Token]):
        self.operators = operators
