__author__ = 'lizheng'
# !/usr/bin/env python
#-*- coding:utf-8 -*-
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('%s\db'%base_dir)

database = {
  "engine":"file",
  "path":"%s\db"%base_dir,
  "log":"%s\log"%base_dir
}