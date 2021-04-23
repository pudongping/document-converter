# -*- coding: utf-8 -*-

'''
文件转换为 pdf
'''

__author__ = 'alex'

import logging

from docx2pdf import convert

from app.helper import *
from app.config.app import AppConfig


class ConverterPdf(object):

    def docx_to_pdf(self, input_path='', output_path=''):
        if (not input_path) and (not output_path): return False
        # 查找指定输入路径下所有的 .docx 文件
        file_list = find_all_file_by_path(AppConfig.DOCX, input_path)

        counter = 0
        for file in file_list:
            file_name = os.path.split(file)[1]  # 文件名 eg: demo1.docx
            pdf_name_with_path = output_path + file_name + '.' + AppConfig.PDF  # 在原文件末尾加上 .pdf 后缀
            msg = '正在处理 <%s> 转换后的文件保存路径为： <%s>' % (file, pdf_name_with_path)
            print(msg)
            logging.info(msg)
            convert(file, pdf_name_with_path)  # docx 转 pdf
            counter += 1

        counter_msg = f'总共需要处理 {len(file_list)} 个文件，{counter} 个文件已经处理完毕！'
        print(counter_msg)
        logging.info(counter_msg)
