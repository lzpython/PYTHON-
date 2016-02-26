__author__ = 'lizheng'
# !/usr/bin/env python
#-*- coding:utf-8 -*-
import json
useracc_dic = {
    'id': 698,
    'passwd': '821620',
    'total': 20000,
    'balance': 20000,
    'start_date': '2015-01-02',
    'end_date': '2020-01-02',
    'pay_day': 24,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}
f = open('698.txt','w')
json.dump(useracc_dic,f)