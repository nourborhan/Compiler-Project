from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        
        
        # Arithmetic Operators
        self.lexer.add("SUM", r'\+')
        self.lexer.add("MINUS", r'-')
        self.lexer.add("MULT", r'\*')
        self.lexer.add("DIV", r'/')

        #Logic Operators
        self.lexer.add("AND", r'\&&')
        self.lexer.add("OR", r'\|\|')
        self.lexer.add("NOT", r'\~')

        #Relational Operators
        self.lexer.add("EQUALS", r'==')
        
        self.lexer.add("MoreThan", r'>')
        self.lexer.add("NOTEQUAL", r'!=')
        self.lexer.add("LessThanOrEqual", r'(<=){1}')
        self.lexer.add("LessThan", r'\<')
        self.lexer.add("MoreThanOrEqual", r'>=')
        # Numbers
        self.lexer.add("NUMBER", r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')

        self.lexer.add("Class", r'Division')
        self.lexer.add("Inheritance", r'InferedFrom')
        self.lexer.add("Condition", r'WhetherDo')
        self.lexer.add("ElseCondition", r'Else')
        self.lexer.add("Integer", r'Ire')
        self.lexer.add("SInteger", r'Sire')
        self.lexer.add("Character", r'Clo')
        self.lexer.add("String", r'SetOfClo')
        self.lexer.add("Float", r'FBU')
        self.lexer.add("SFloat", r'SFBU')
        self.lexer.add("Void", r'NoneValue')
        self.lexer.add("Break", r'TerminateThisNow')
        self.lexer.add("Loop", r'RingWhen')
        self.lexer.add("Return", r'BackedValue')
        self.lexer.add("Struct", r'STT')
        self.lexer.add("Switch", r'Check-CaseOf')
        self.lexer.add("Start_Statement", r'Beginning')
        self.lexer.add("End_Statement", r'End')
        self.lexer.add("Assign", r'\=')
        self.lexer.add("Access", r'\.')
        self.lexer.add("CurlyOpen", r'\{')
        self.lexer.add("CurlyClose", r'\}')
        self.lexer.add("SquareOpen", r'\[')
        self.lexer.add("SquareClose", r'\]')
        self.lexer.add("DoubleQuote", r'\"')
        self.lexer.add("SingleQuote", r"\'")
        self.lexer.add("Inclusion", r'Using')
        # self.lexer.add("MultiLineCommentOpen", r'(\/#){1}')
        # self.lexer.add("MultiLineCommentClose", r'(#\){1}')
        # self.lexer.add("SingleComment", r'(\/-){1}')
        self.lexer.add("TokenDelimiter", r'\@')
        self.lexer.add("LineDelimiter", r'\;')
        self.lexer.add("OpenBrace", r'\(')
        self.lexer.add("CloseBrace", r'\)')
        self.lexer.add("Empty", r'empty')
        self.lexer.add("Comma", r'\,')
        self.lexer.add("Read", r'read')
        self.lexer.add("Write", r'write')

        self.lexer.add("ID", r'\w+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()