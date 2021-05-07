from lexer import Lexer
# from parserTB import Parser


text_input = """
Ire@X=2;
FBU@Y=2.2;
"""



lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
lines = tokens.s.splitlines()

# LineNumber = 0
# TokenNumber = 1
# for line in lines:
#     LineTokens = lexer.lex(line)
#     for token in LineTokens:
#         tokenStream = {
#             "Line No": LineNumber,
#             "Lexeme": token.value,
#             "Return Token": token.name,
#             "Lexeme NO in line": TokenNumber,
#             "Matchability": "Matched"
#         }
#         print(tokenStream)
#         TokenNumber += 1
#     LineNumber += 1
#     TokenNumber = 1


    # print(token.getstr())


# for token in tokens:
#     print(token)


# pg = Parser()
# pg.parse()
# parser = pg.get_parser()
# parser.parse(tokens).eval()