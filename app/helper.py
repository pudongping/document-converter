# -*- coding: utf-8 -*-

'''
助手函数
'''

__author__ = 'alex'

import os
from pathlib import Path


def find_all_file_by_path(suffix='', path=''):
    '''
    查找出指定目录下指定文件后缀的所有文件
    :param suffix: 文件名后缀
    :param path: 指定目录，当不指定目录时，则默认为当前目录
    :return: 所有指定后缀文件列表
    '''
    if not suffix: return []
    if (not bool(path)):
        path = os.getcwd() + os.sep  # 当前目录绝路路径
    p = Path(path)  # 初始化构造 Path 对象
    file_list = list(p.glob('*.' + suffix))  # 查找出指定目录下指定文件后缀的所有文件
    return file_list


def mkdir(dir=''):
    '''
    创建目录
    :param dir: 需要创建的目录字符串
    :return:
    '''
    if not dir: return False
    if not os.path.exists(dir):
        os.makedirs(dir)
    return True
