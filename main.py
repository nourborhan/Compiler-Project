from lexer import Lexer
from parserTB import Parser
from ast import Parser_Output


# text_input = """
# Beginning;
# Division@x{
#     Ire@decrease(){
#         Ire@reg3=5;
#         RingWhen(counter < num){
#             reg3 = reg3 -1;
#         }
#     }
# }
# End
# """

text_input = """
Beginning;
Division@main{Ire@X;};
End
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
        TokenNumber = TokenNumber + 1
    pg = Parser()
    pg.parse(TokenStream,LineNumber)
    LineNumber = LineNumber + 1
    TokenNumber = 1

for line in TokenStream:
    print(line)

parser = pg.get_parser()
parser.parse(tokens)

# for obj in TokenStream:
#    print(obj)

# print(lineno)
# TokenLines = TokenStream["Line No"]

# print(TokenStream)
    

# for token in tokens:
#     print(token)

# pg = Parser()
# pg.parse(TokenStream)
# parser = pg.get_parser()
# parser.parse(tokens)

