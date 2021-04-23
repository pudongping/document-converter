#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
项目入口文件
'''

__author__ = 'alex'

import logging
import os
import datetime

from app.config.app import AppConfig
from app.converter.converter_pdf import ConverterPdf

APP_PATH = os.path.abspath('.')  # 项目绝对路径

def init_log():
    log_rel_dir = 'runtime' + os.sep + 'logs' + os.sep + datetime.datetime.now().strftime('%Y%m')
    log_abs_dir = os.path.join(APP_PATH, log_rel_dir)
    if not os.path.exists(log_abs_dir):
        os.makedirs(log_abs_dir)

    log_file = log_abs_dir + os.sep + 'converter-' + datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
    logging.basicConfig(
        level=logging.DEBUG,
        filename=log_file,
        datefmt='%Y-%m-%d %H:%M:%S',
        format="[%(asctime)s] %(name)s.%(levelname)s : %(filename)s ==> [%(lineno)d] : the message is => [ %(message)s ]"
    )

def docx_to_pdf():
    logging.info('docx 转 pdf')
    i = AppConfig().input_docx()
    o = AppConfig().output_pdf()
    ConverterPdf().docx_to_pdf(i, o)

def main():
    init_log()

    print(not bool({}))




if __name__ == '__main__':
    main()