from rply import ParserGenerator
# from ast import Print
from ast import Parser_Output

#       ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
#              'SEMI_COLON', 'SUM']

class Parser():

        def __init__(self):
            self.pg = ParserGenerator(
                # A list of all token names accepted by the parser.
                ["SUM","MINUS","MULT","DIV","AND","OR","NOT","EQUALS","LessThan","MoreThan","NUMBER","Class","Inheritance"
                ,"IfCondition","ElseCondition","Integer","SInteger","Character","String","Float","SFloat","Void","Break","Loop",
                "Return","Struct","Switch","Start_Statement","End_Statement","Assign","Access","CurlyOpen","CurlyClose"
                ,"SquareOpen","SquareClose","DoubleQuote","SingleQuote","Inclusion",
                "TokenDelimiter","LineDelimiter","OpenBrace","CloseBrace","ID","SingleComment","Comma","Read","Write",
                "LessThanOrEqual","MoreThanOrEqual", "NOTEQUAL", "MultiLineCommentOpen", "MultiLineCommentClose","txt","Empty"
                ]
            )

        def parse(self,TokenStream,LineNumber):
            
            @self.pg.production('program : Start_Statement LineDelimiter ClassDeclaration LineDelimiter End_Statement')
            @self.pg.production('program : SingleComment LineDelimiter using_command')
            def program(p):
                start = p[0]
                end = p[4]
                if start.name == "Start_Statement" and end.name == "End_Statement":
                    # return print("Rule Used: Program")
                    output = Parser_Output(TokenStream)
                    return print(output.Output_Formation("True","Program",LineNumber)) 
                elif start.name == "SingleComment":
                    output = Parser_Output(TokenStream)
                    return print(output.Output_Formation("True","Program",LineNumber)) 
                    # return print("Rule Used: Program")
                # start = p[0]
                # if start.gettokentype() == 'Start_Statement' and p[1].name == 'LineDelimiter' and p[2].name == 'Class' and p[3].name == 'LineDelimiter' and p[4].name == 'End_Statement':
                #     return print("Match: Rule Used: Program")
                # elif start.gettokentype() == 'Start_Statement' and p[1].name == 'LineDelimiter' and p[2].name == 'using_command':
                #     return print("Match: Rule Used: Program")
                # else:
                #      return print("program")
                       
                
            @self.pg.production('Type : Integer')
            @self.pg.production('Type : SInteger')
            @self.pg.production('Type : Character')
            @self.pg.production('Type : String')
            @self.pg.production('Type : Float')
            @self.pg.production('Type : SFloat')
            @self.pg.production('Type : Void')
            def Type(p):
                # return print("Rule Used: Type")
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Type",LineNumber))                                     

            @self.pg.production('ClassDeclaration : Class TokenDelimiter ID CurlyOpen Class_Implementation CurlyClose')
            @self.pg.production('ClassDeclaration : Class TokenDelimiter ID TokenDelimiter Inheritance CurlyOpen Class_Implementation CurlyClose')
            def ClassDeclaration(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Class_Decl",LineNumber)) 
                # return print("Rule Used: Class_Decl") 

            # @self.pg.production('Class_Implementation : Var_Declaration Class_Implementation')
            @self.pg.production('Class_Implementation : Var_Declaration')
            @self.pg.production('Class_Implementation : Method_Declaration')
            @self.pg.production('Class_Implementation : SingleComment')
            @self.pg.production('Class_Implementation : Func_Call')
            @self.pg.production('Class_Implementation : Empty')
            def ClassImplementation(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Class_Implementation",LineNumber)) 
                # return print("Rule Used: Class_Implement")


            @self.pg.production('Method_Declaration : Func_Decl LineDelimiter')
            @self.pg.production('Method_Declaration : Func_Decl CurlyOpen Var_Declaration Statements CurlyClose')
            def Method_Declaration(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Method_Decl",LineNumber)) 

            @self.pg.production('Func_Decl : Type TokenDelimiter ID OpenBrace Parameter_List CloseBrace')
            def Func_Decl(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Func_Decl",LineNumber)) 

            @self.pg.production('Parameter_List : Empty')
            @self.pg.production('Parameter_List : Void')
            @self.pg.production('Parameter_List : Non_Empty_List')
            def ParameterList(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Par_List",LineNumber)) 

            @self.pg.production('Non_Empty_List : Type TokenDelimiter ID')
            @self.pg.production('Non_Empty_List : Non_Empty_List TokenDelimiter ID_List LineDelimiter Var_Declaration')
            def Non_Empty_List(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Non_Empty_List",LineNumber)) 

            @self.pg.production('ID_List : ID')
            # @self.pg.production('ID_List : ID_List Comma ID')
            def ID_List(p):
                # return print("Rule Used: ID_List")
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","ID_List",LineNumber)) 

            @self.pg.production('Var_Declaration : Empty')
            # @self.pg.production('Var_Declaration : Type TokenDelimiter ID_List LineDelimiter Var_Declaration')
            @self.pg.production('Var_Declaration : Type TokenDelimiter ID_List LineDelimiter')
            def Var_Declaration(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Var_Decl",LineNumber)) 
                # return print("Rule Used: Var_Decl")

            @self.pg.production('Statements : Empty')
            @self.pg.production('Statements : Statement Statements')
            def Statements(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Statements",LineNumber)) 


            @self.pg.production('Statement : Assignment')
            @self.pg.production('Statement : WhetherDo_Statement')
            @self.pg.production('Statement : RingWhen_Statement')
            @self.pg.production('Statement : BackedValue_Statement')
            @self.pg.production('Statement : terminateThis_Statement')
            @self.pg.production('Statement : Read OpenBrace ID CloseBrace LineDelimiter')
            @self.pg.production('Statement : Write OpenBrace Expression CloseBrace LineDelimiter')
            def Statement(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Statement",LineNumber)) 


            @self.pg.production('Assignment : Var_Declaration Assign Expression LineDelimiter')
            def Assignment(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Assignment",LineNumber)) 

            @self.pg.production('Func_Call : ID OpenBrace Argument_List CloseBrace LineDelimiter')
            def Func_Call(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Func_Call",LineNumber)) 

            @self.pg.production('Argument_List : Empty')
            @self.pg.production('Argument_List : NonEmpty_Argument_List')
            def Argument_List(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Arg_List",LineNumber)) 

            @self.pg.production('NonEmpty_Argument_List : Expression')
            @self.pg.production('NonEmpty_Argument_List : NonEmpty_Argument_List Comma Expression')
            def NonEmpty_Argument_List(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","NoneEmpty_ArgList",LineNumber)) 

            @self.pg.production('BlockStatements : CurlyOpen Statements CurlyClose')
            def BlockStatements(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Block_Statements",LineNumber)) 


            @self.pg.production('WhetherDo_Statement : Condition OpenBrace Condition_Expression CloseBrace BlockStatements ElseCondition Statement')
            def WhetherDo_Statement(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","WhetherDo",LineNumber)) 


            @self.pg.production('Condition_Expression : Condition')
            @self.pg.production('Condition_Expression : Condition Condition_Op')
            def Condition_Expression(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Cond_Expr",LineNumber)) 

            @self.pg.production('Condition_Op : AND')
            @self.pg.production('Condition_Op : OR')
            def Condition_Op(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Cond_Op",LineNumber)) 


            @self.pg.production('Condition : Expression Comparison_Op Expression')
            def Condition(p):
                return print("body")


            @self.pg.production('Comparison_Op : EQUALS')
            @self.pg.production('Comparison_Op : NOTEQUAL')
            @self.pg.production('Comparison_Op : LessThan')
            @self.pg.production('Comparison_Op : MoreThan')
            @self.pg.production('Comparison_Op : LessThanOrEqual')
            @self.pg.production('Comparison_Op : MoreThanOrEqual')
            def Comparison_Op(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Comp_Op",LineNumber)) 

            @self.pg.production('RingWhen_Statement : Loop OpenBrace Condition_Expression CloseBrace BlockStatements')
            def RingWhen_Statement(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","RingWhen",LineNumber)) 

            @self.pg.production('BackedValue_Statement : Void TokenDelimiter Expression LineDelimiter')
            @self.pg.production('BackedValue_Statement : Void TokenDelimiter ID LineDelimiter')
            def BackedValue_Statement(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","BackedValue",LineNumber)) 


            @self.pg.production('terminateThis_Statement : Break LineDelimiter')
            def terminateThis_Statement(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Terminate",LineNumber)) 


            @self.pg.production('Expression : Term')
            @self.pg.production('Expression : Expression TokenDelimiter Add_Op TokenDelimiter Term')
            def Expression(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Expression",LineNumber)) 


            @self.pg.production('Add_Op : SUM')
            @self.pg.production('Add_Op : MINUS')
            def Add_Op(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Add_Op",LineNumber)) 

            @self.pg.production('Term : Factor')
            @self.pg.production('Term : Term TokenDelimiter Mul_Op TokenDelimiter Factor')
            def Term(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Term",LineNumber)) 


            @self.pg.production('Mul_Op : MULT')
            @self.pg.production('Mul_Op : DIV')
            def Mul_Op(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Mul_Op",LineNumber)) 


            @self.pg.production('Factor : ID')
            @self.pg.production('Factor : NUMBER')
            def Factor(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Factor",LineNumber)) 

            @self.pg.production('Comment : MultiLineCommentOpen String MultiLineCommentClose')
            @self.pg.production('Comment : SingleComment String')
            def Comment(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Comment",LineNumber)) 


            @self.pg.production('using_command : Inclusion OpenBrace F_name Access txt CloseBrace LineDelimiter')
            def using_command(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","Using",LineNumber)) 

            @self.pg.production('F_name : String')
            def F_name(p):
                output = Parser_Output(TokenStream)
                return print(output.Output_Formation("True","F_Name",LineNumber)) 



            @self.pg.error
            def error_handle(token):
                raise ValueError("Total No of errors: 1")
                # raise ValueError(token)
                # raise ValueError("No Match")
                

        def get_parser(self):
            return self.pg.build()
