from lexer import Lexer
from parserTB import Parser

text_input = """
print(8 + 5);

division car(){

}
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()