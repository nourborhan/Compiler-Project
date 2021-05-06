from rply import ParserGenerator
from ast import Number, Sum, Print

#       ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
#              'SEMI_COLON', 'SUM']

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ["SUM","MINUS","MULT","DIV","AND","OR","NOT","EQUALS","LessThan","MoreThan","NUMBER","Class","Inheritance"
            ,"Condition","ElseCondition","Integer","SInteger","Character","String","Float","SFloat","Void","Break","Loop",
             "Return","Struct","Switch","Start_Statement","End_Statement","Assign","Access","CurlyOpen","CurlyClose"
             ,"SquareOpen","SquareClose","DoubleQuote","SingleQuote","Inclusion",
             "TokenDelimiter","LineDelimiter","OpenBrace","CloseBrace","Identifier","SingleComment"
             ]
        )

    def parse(self):
        # @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        # def program(p):
        #     return Print(p[2])

        @self.pg.production('program : Start_Statement LineDelimiter Class LineDelimiter End_Statement')
        @self.pg.production(': ')
        def program(p):
            #return Print(p[2])


        @self.pg.production('class: Class TokenDelimiter Identifier OpenBrace CloseBrace CurlyOpen CurlyClose')
        def division(p):

        # @self.pg.production('expression : expression SUM expression')
        # def expression(p):
        #     left = p[0]
        #     right = p[2]
        #     operator = p[1]
        #     if operator.gettokentype() == 'SUM':
        #         return Sum(left, right)



        # @self.pg.production('expression : NUMBER')
        # def number(p):
        #     return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()