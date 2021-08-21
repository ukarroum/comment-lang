from enum import Enum, auto

class TokenType(Enum):
	# available data types
	INT = auto() 

	# two ways to put a comment
	COMMENT_SLASH = auto() # //
	COMMENT_DASH = auto() # //

	# operators
	ADD = auto()

class Token:
	def __init__(self, lexeme: str, token_type: TokenType, line: int):
		self.lexeme = lexeme
		self.token_type = token_type
		self.line = line
	
	def __repr__(self):
		return f"{self.token_type} : {self.lexeme}"
