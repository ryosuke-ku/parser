import logging.config
from ast.ast_processor import AstProcessor
from ast.basic_info_listener import BasicInfoListener
import glob
import re
import os


if __name__ == '__main__':
    # target_file_path = 'C:/pbl/home/junit/src/test/java/jp/enpit/cloud/junit/CalculatorTest.java'
    target_file_path = 'C:/Users/ryosuke-ku/Desktop/NiCad-5.1/systems/maven/maven-model-builder/src/test/java/org/apache/maven/model/interpolation/StringSearchModelInterpolatorTest.java'
    # target_file_path = 'C:/Users/ryosuke-ku/Desktop/NiCad-5.1/systems/maven/maven-model-builder/src/main/java/org/apache/maven/model/interpolation/StringSearchModelInterpolator.java'
    TestPaths = glob.glob('D:/ryosuke-ku/data_set/ant_20190607/ant/**/*Test.java', recursive=True)

    ast_info = AstProcessor(None, BasicInfoListener()).execute(target_file_path)
    # for TestPath in TestPaths:
    #     ast_info = AstProcessor(None, BasicInfoListener()).execute(TestPath)
