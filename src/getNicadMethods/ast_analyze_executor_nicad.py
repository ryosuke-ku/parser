import logging.config
from ast.ast_processor_production_nicad import AstProcessor
from ast.basic_info_listener_nicad import BasicInfoListener
import glob
import re
import os


if __name__ == '__main__':
    target_file_path = 'C:/Users/ryosuke-ku/Desktop/SCRAPING/Method_Scraping/NicadMethods.java'
    # target_file_path = 'C:/Users/ryosuke-ku/Desktop/NiCad-5.1/systems/maven/maven-model-builder/src/test/java/org/apache/maven/model/interpolation/StringSearchModelInterpolatorTest.java'
    ast_info = AstProcessor(None, BasicInfoListener()).execute(target_file_path)

    