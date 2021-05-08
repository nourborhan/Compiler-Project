from lexer import Lexer
from parserTB import Parser


# text_input = """
# Ire@X=2;
# FBU@Y=2.2;
# """


# text_input = """
# Beginning;Division;End
# """
text_input = """
Ire
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
lines = tokens.s.splitlines()

TokenStream = []
LineNumber = 0
TokenNumber = 1
for line in lines:
    LineTokens = lexer.lex(line)
    for token in LineTokens:
        SingleToken = {
            "Line No": LineNumber,
            "Lexeme": token.value,
            "Return Token": token.name,
            "Lexeme NO in line": TokenNumber,
            "Matchability": "Matched"
        }
        TokenStream.append(SingleToken)
        TokenNumber += 1
    LineNumber += 1
    TokenNumber = 1

# for obj in TokenStream:
#     print(obj)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)  