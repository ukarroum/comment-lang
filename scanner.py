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
			
			# COMMENT_SLASH
			elif code[position] == '/':
				position += 1
				if code[position] == '/':
					tokens.append(Token('//', TokenType.COMMENT_SLASH, line))
					position += 1
				else:
					raise ComSyntaxException(f"Invalid comment literal at line {line}")

			# COMMENT_DASH
			elif code[position] == '#':
				tokens.append(Token('#', TokenType.COMMENT_DASH, line))
				position += 1

			# ADD
			elif code[position] == '+':
				tokens.append(Token('+', TokenType.ADD, line))
				position += 1

			if code[position] == '\n':
				line += 1
			if code[position] in [' ', '\n']:
				position += 1

		return tokens
	
	
