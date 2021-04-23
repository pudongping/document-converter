# -*- coding: utf-8 -*-

'''
配置文件信息
'''

__author__ = 'alex'

import os

from app.helper import mkdir


class AppConfig(object):
    DOCX = 'docx'
    PDF = 'pdf'

    @classmethod
    def __get_default_input_path(cls):
        input = os.path.abspath('.') + os.sep + 'data' + os.sep + 'input' + os.sep
        mkdir(input)
        return input

    @classmethod
    def __get_default_output_path(cls):
        output = os.path.abspath('.') + os.sep + 'data' + os.sep + 'output' + os.sep
        mkdir(output)
        return output

    def input_docx(self):
        return AppConfig.__get_default_input_path() + self.__class__.DOCX + 's' + os.sep

    def output_pdf(self):
        return AppConfig.__get_default_output_path() + self.__class__.PDF + 's' + os.sep
