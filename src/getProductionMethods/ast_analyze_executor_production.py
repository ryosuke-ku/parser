import logging.config
from ast.ast_processor_production import AstProcessor
from ast.ast_processor2_production import AstProcessor2
from ast.basic_info_listener_production import BasicInfoListener
import glob
import re
import os


if __name__ == '__main__':
    # target_file_path = 'C:/pbl/home/junit/src/test/java/jp/enpit/cloud/junit/CalculatorTest.java'
    target_file_path = 'C:/Users/ryosuke-ku/Desktop/NiCad-5.1/systems/maven/maven-model-builder/src/test/java/org/apache/maven/model/interpolation/StringSearchModelInterpolatorTest.java'
    # target_file_path = 'C:/Users/ryosuke-ku/Desktop/NiCad-5.1/systems/maven/maven-model-builder/src/main/java/org/apache/maven/model/interpolation/StringSearchModelInterpolator.java'

    # l = glob.glob('C:/Users/ryosuke-ku/Desktop/PARSER/src/**/*.py', recursive=True)
    # l = glob.glob('C:/Users/ryosuke-ku/Desktop/sample-project/**/*.java', recursive=True)
    # TestPaths = glob.glob('D:/ryosuke-ku/data_set/ant_20190607/ant/**/*Test.java', recursive=True)
    # AllPaths = glob.glob('D:/ryosuke-ku/data_set/ant_20190607/ant/**/*.java', recursive=True)
    TestPaths = glob.glob('C:/Users/ryosuke-ku/Desktop/NiCad-5.1/systems/maven/maven-model-builder/src/main/java/org/apache/maven/model/interpolation/**/*Test.java', recursive=True)
    ProductionPath = 'C:/Users/ryosuke-ku/Desktop/NiCad-5.1/systems/maven/maven-model-builder/src/main/java/org/apache/maven/model/interpolation/StringSearchModelInterpolator.java'
    # target_file_path = 'C:/Users/ryosuke-ku/Desktop/a2.java'

    # ProductionPaths = list(set(AllPaths) - set(TestPaths))
    # print(ProductionPaths)
    # print(TestPaths)
    # print(ProductionPaths)
    # print(len(AllPaths))
    # print(len(TestPaths))
    # print(len(ProductionPaths))
    # print(len(TestPaths))
    ast_info = AstProcessor(None, BasicInfoListener()).execute(target_file_path)

    # ast_info = AstProcessor2(None, BasicInfoListener()).execute(ProductionPath)
    # for ProductionPath in ProductionPaths:
    #     ast_info = AstProcessor(None, BasicInfoListener()).execute(ProductionPath)
    