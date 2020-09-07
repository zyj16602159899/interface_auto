#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Author：zhuxiujie
import configparser
import os
from tools.project_path import conf_dir

config_file = os.path.join(conf_dir, 'config.ini')


class ReadConfig:
    """封装读取和写入config文件的方法"""

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(config_file, encoding='utf-8')

    def read_config(self, option, section):
        """读取配置文件数据"""
        return self.conf[option][section]

    def write_back_data(self, option, section, value):
        """写入配置文件数据"""
        self.conf.set(option, section, value)
        with open(config_file, 'w', encoding='utf-8') as file:
            self.conf.write(file)
