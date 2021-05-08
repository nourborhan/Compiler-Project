from lexer import Lexer
# from parserTB import Parser


text_input = """
Ire@X=2;
FBU@Y=2.2;
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

for obj in TokenStream:
    print(obj)