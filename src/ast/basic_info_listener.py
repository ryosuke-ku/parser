from ast.JavaParserListener import JavaParserListener
from ast.JavaParser import JavaParser
import re

# ★ポイント３
class BasicInfoListener(JavaParserListener):

    # ★ポイント４
    def __init__(self):
        self.call_methods = []
        self.ast_info = {
            'methods': []
        }

    # Exit a parse tree produced by JavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):

        # ★ポイント６
        # c1 = ctx.getChild(0).getText()  # ---> return type
        # c2 = ctx.getChild(1).getText()  # ---> method name
        print(ctx.getChild(1).getText())
        # line_number = str(ctx.start.line)
        # column_number = str(ctx.start.column)
        # c3 = ctx.getChild(2).getText()  # ---> params
        # params = self.parse_method_params_block(ctx.getChild(2))

        # method_info = {
        #     # 'returnType': c1,
        #     'methodName': c2,
        #     # 'methodName': c2 + ' ' + line_number + ' ' + column_number,
        #     # 'params': params,
        #     'callMethods': self.call_methods
        # }
        # self.ast_info['methods'].append(method_info)

    # Enter a parse tree produced by JavaParser#methodCall.
    def enterMethodCall(self, ctx:JavaParser.MethodCallContext):
        # ★ポイント７
        # line_number = str(ctx.start.line)
        # column_number = str(ctx.start.column)
        # self.call_methods.append(line_number + ' ' + column_number + ' ' + ctx.parentCtx.getText())
        # self.call_methods.append(ctx.parentCtx.getText())
        cmName = ctx.parentCtx.getText()
        if 'assert' in ctx.parentCtx.getText():
            pass
        else:
            # print(cmName)
            # re.sub(r".*?\.","",cmname)
            s = cmName.rfind('.')
            # print(s)
            # print(cmname[:s])
            editcmName = cmName[s+1:]
            # print(editcmName)

            b = editcmName.find('(')
            # print(b)
            fincmName = editcmName[:b]
            # print(fincmName)
            # print(re.sub(r".*?\.","",cmname))
