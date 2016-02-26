__author__ = 'lizheng'
# !/usr/bin/env python
#-*- coding:utf-8 -*-


#from mall.bin import mall_service
from ATM.bin import main
from MALL.bin import shoppingservice

while True:
    print("***********欢迎访问购物平台***********\n1.ATM服务\n2.购物商城\n3.退出")
    user_choose = input('请输入类型序号>>')
    if user_choose == '1':
        main.run(0)
    elif user_choose == '2':
        shoppingservice.run()
    elif user_choose == '3':
        break





