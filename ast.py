class Parser_Output():

    def __init__(self, TokenStream):
        self.TokenStream = TokenStream



    def Output_Formation(self, isMatch, Rule, LineNumber):
        # TokenLineNo = []
        # ListOfLines = []
        # for token in self.TokenStream:
        #     TokenLineNo.append(token["Line No"])

        # for LineNo in TokenLineNo:
        #     if LineNo > LineNumber:
        #         LineNumber = LineNo

        # lineCount = 1
        
        # for line in range(LineNumber):
        print ("{:<20} {:<20} {:<20}".format(LineNumber, Rule, isMatch))
        # singleLine = {
        #     "Line NO": LineNumber,
        #     "Matchability": isMatch,
        #     "Rule Used": Rule
        # }
        
            # ListOfLines.append(singleLine)
            # lineCount += 1
        # return singleLine


# class Number():
#     def __init__(self, value):
#         self.value = value
#
#     def eval(self):
#         return int(self.value)
#
#
# class BinaryOp():
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
#
# class Sum(BinaryOp):
#     def eval(self):
#         return self.left.eval() + self.right.eval()
#
#
# class Print():
#     def __init__(self, value):
#         self.value = value
#
#     def eval(self):
#         print(self.value.eval())
#
# class Program():
#     def __init__(self, value):
#         self.value = value
