from lexer import Lexer
# from parserTB import Parser


text_input = """
RingWhen (x < y) { BackedValue 2; }
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)


for token in tokens:
    print(token)


# pg = Parser()
# pg.parse()
# parser = pg.get_parser()
# parser.parse(tokens).eval()