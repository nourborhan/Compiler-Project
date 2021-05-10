from lexer import Lexer
from parserTB import Parser
import warnings
warnings.filterwarnings("ignore")


lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    elif line == "End":
        break
    else:
        break
text_input = '\n'.join(lines)

# text_input = """
# Beginning;
# Division@main{Ire@X;};
# End
# """


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

# text_input = """
# Beginning;
# Division@main{Ire@X(empty);};
# End
# """
   
print("Scanner output \n")

print ("{:<10} {:<10} {:<20} {:<25} {:<10}".format('LineNO', 'Lexeme ', 'Token','Lexeme in line number','Matchability'))
lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
lines = tokens.s.splitlines()

SingleToken = {}
LineNumber = 1
TokenNumber = 1
counter = 0
for line in lines:
    LineTokens = lexer.lex(line)
    for token in LineTokens:

        print ("{:<10} {:<10} {:<21} {:<25} {:<10}".format(LineNumber, token.value, token.name,TokenNumber,"Matched"))

        SingleToken[counter] = [LineNumber,token]
        TokenNumber = TokenNumber + 1
        counter = counter + 1    
    pg = Parser()
    pg.parse(SingleToken)
    LineNumber = LineNumber + 1
    TokenNumber = 1
    
print("\n")
print("Parser Output \n")
print ("{:20} {:<20} {:<20}".format('Line Number', 'Rule Used ', 'Matchability'))
parser = pg.get_parser()
parser.parse(tokens)

