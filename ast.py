# class Parser_Output():
#     ListOfLines = []
#     def Output_Formation(TokenStream,isMatch,Rule):

#         LineNumber = 0
#         for token in TokenStream:
#             if token["Line No"] > LineNumber:
#                 LineNumber = token["Line No"]

#         lineCount = 1
#         for line in range(LineNumber):
#             singleLine = {
#                 "Line NO": lineCount,
#                 "Matchability": isMatch,
#                 "Rule Used": Rule
#             }
#             ListOfLines.append(singleLine)
#             lineCount += 1
#         return ListOfLines
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
