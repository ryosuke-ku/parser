from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from ast.JavaLexer import JavaLexer
from ast.JavaParser import JavaParser
from pprint import pformat
from ast.ast_processor2_production import AstProcessor2
from ast.basic_info_listener_production import BasicInfoListener
import re

class rdict(dict):
    def __getitem__(self, key):
        try:
            return super(rdict, self).__getitem__(key)
        except:
            try:
                ret=[]
                for i in self.keys():
                    m= re.match("^"+key+"$",i)
                    if m:ret.append( super(rdict, self).__getitem__(m.group(0)) )
            except:raise(KeyError(key))
        return ret

class AstProcessor:

    def __init__(self, logging, listener):
        # self.logging = logging
        # self.logger = logging.getLogger(self.__class__.__name__)
        self.listener = listener

    # ★ポイント２
    def execute(self, input_source):
        parser = JavaParser(CommonTokenStream(JavaLexer(FileStream(input_source, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.compilationUnit())
        # self.logger.debug('Display all data extracted by AST. \n' + pformat(self.listener.ast_info, width=160))
        # print(self.listener.ast_info)
        # print(self.listener.call_methods)
        # print(self.listener.called_methods)
        # print(self.listener.called_methods['setUp'])
        # print(self.listener.methods['testLocationTrackerShouldBeExcludedFromInterpolation'])
        # print(len(self.listener.methods['testLocationTrackerShouldBeExcludedFromInterpolation']))
        # print(sum(len(v) for v in self.listener.called_methods['testLocationTrackerShouldBeExcludedFromInterpolation']))
        # print(self.listener.methods)
        cnt = 1
        listmethods =[]
        listcallmethods = []
        ProductionPath = 'C:/Users/ryosuke-ku/Desktop/NiCad-5.1/systems/maven/maven-model-builder/src/main/java/org/apache/maven/model/interpolation/StringSearchModelInterpolator.java'
        for method in self.listener.methods:
            num = len(self.listener.called_methods[method][0])
            # print(num)

            for i in range(num):
                print(method + '/' + self.listener.called_methods[method][0][i])
                listmethods.append(method)
                listcallmethods.append(str(cnt) + ' ' + self.listener.called_methods[method][0][i])
                cnt +=1

        d = dict(zip(listcallmethods,listmethods))
        # print(d)

        rd = rdict(d)
        

        # print(listmethods)
        # print(len(listmethods))
        # print(listcallmethods)
        # print(len(listcallmethods))
        methods_list = AstProcessor2(None, BasicInfoListener()).execute(ProductionPath)
        print(methods_list)
        print('------------------------')

        for key in methods_list:
            # print(key)
            
            if rd["^(?=.*" + key + ").*$"] == []:
                pass
            
            else:
                print(key)
                print(rd["^(?=.*" + key + ").*$"])
                print(len(rd["^(?=.*" + key + ").*$"]))
        

        # return self.listener.ast_info