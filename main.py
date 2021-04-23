#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
项目入口文件
'''

__author__ = 'alex'
__version__ = '0.0.1'

import logging
import os
import datetime
import sys
from multiprocessing import Process

from app.config.app import AppConfig
from app.converter.converter_pdf import ConverterPdf
from app.converter.converter_docx import ConverterDocx


def init_log():
    '''
    初始化日志配置
    :return:
    '''
    log_rel_dir = 'runtime' + os.sep + 'logs' + os.sep + datetime.datetime.now().strftime('%Y%m')
    log_abs_dir = os.path.join(os.path.abspath('.'), log_rel_dir)
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
    '''
    docx 转 pdf
    :return:
    '''
    logging.info('docx 转 pdf')
    i = AppConfig().input_docx()
    o = AppConfig().output_pdf()
    ConverterPdf().docx_to_pdf(i, o)


def pdf_to_docx():
    '''
    pdf 转 docx（不支持图片提取）
    :return:
    '''
    logging.info('pdf 转 docx')
    i = AppConfig().input_pdf()
    o = AppConfig().output_docx()
    ConverterDocx().pdf_to_docx(i, o)


def command_args_msg():
    return 'usage: python3 main.py [--version] [-h] [--docx-to-pdf] [--pdf-to-docx]'


def help_doc():
    msg = command_args_msg()
    msg += '''
    
    These are common App commands used in various situations:
    
    Options:
    
    --version           Show this app's version
    --help or -h        Show help documents
    --docx-to-pdf       Docx documents are converted to PDF documents
    --pdf-to-docx       PDF documents are converted to Docx documents
    
    '''
    print(msg)


def handle_command(command):
    '''
    处理命令参数
    :param command:
    :return:
    '''
    if command in ('--help', '-h'):
        help_doc()
    elif '--version' == command:
        print(f'python version is 3.8 and this app version is {__version__}')
    elif '--docx-to-pdf' == command:
        print(f'''First, you should move the docx file to <{AppConfig().input_docx()}> folder''')
        is_ok = input('Proceed (y/n)? ')
        if 'y' != is_ok.lower(): exit(0)
        p = Process(target=docx_to_pdf())
        p.start()
    elif '--pdf-to-docx' == command:
        print(f'''First, you should move the docx file to <{AppConfig().input_pdf()}> folder''')
        is_ok = input('Proceed (y/n)? ')
        if 'y' != is_ok.lower(): exit(0)
        p = Process(target=pdf_to_docx())
        p.start()
    else:
        print(command_args_msg())


def main():
    init_log()
    args = sys.argv
    if len(args) == 1:
        help_doc()
    elif len(args) == 2:
        handle_command(args[1])
    else:
        print(command_args_msg())


if __name__ == '__main__':
    main()
