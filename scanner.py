from token import Token, TokenType
from errors import ComSyntaxException

class Scanner:
    def __init__(self, source: str):
        self.source = source

    def scan_tokens(self):
        tokens = []

        line = 1
        position = 0

        with open(self.source) as f:
            code = f.read()

        while position < len(code):
            # INT
            if code[position].isdigit():
                dig = code[position]
                position += 1

                while position < len(code) and code[position].isdigit():
                    dig += code[position]
                    position += 1
                if code[position] in [' ', '\n']:
                    tokens.append(Token(dig, TokenType.INT, line))
                else:
                    raise ComSyntaxException(f"Invalid integer literal at line {line}")

            elif code[position] == '"':
                string = ""
                position += 1
                # we dont allow multiline strings 
                # speaking of usability
                while position < len(code) and code[position] not in ['"', '\n']:
                    string += code[position]
                    position += 1
                if position == len(code) or code[position] == '\n':
                    raise ComSyntaxException(f"Invalid string literal at line {line}")
                else:
                    tokens.append(Token(string, TokenType.STR, line))
                    position += 1
            
            # COMMENT_SLASH and DIV
            elif code[position] == '/':
                position += 1
                if code[position] == '/':
                    tokens.append(Token('//', TokenType.COMMENT_SLASH, line))
                    position += 1
                else:
                    tokens.append(Token('/', TokenType.DIV, line))

            # COMMENT_DASH
            elif code[position] == '#':
                tokens.append(Token('#', TokenType.COMMENT_DASH, line))
                position += 1

            # ADD
            elif code[position] == '+':
                tokens.append(Token('+', TokenType.ADD, line))
                position += 1
            elif code[position] == '-':
                tokens.append(Token('-', TokenType.SUB, line))
                position += 1
            elif code[position] == '*':
                tokens.append(Token('*', TokenType.MUL, line))
                position += 1

            if code[position] == '\n':
                line += 1
            if code[position] in [' ', '\n']:
                position += 1

        return tokens
    
    
