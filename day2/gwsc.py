__author__ = 'thinkpad'
__author__ = 'lizheng'
# !/usr/bin/env python
#-*- coding:utf-8 -*-

user_file = open('user','r+')
user_line = user_file.readlines()
flag = True
comm_dict = {'洗衣机':'1800','电饭堡':'300','自行车':'1200'}
list = []
while flag:
    print("欢迎登陆购物商场".center(50,'*'))
    us = input(">>请输入用户名：")
    pwd = input(">>请输入密码：")
    for item in user_line:
#生成用户列表
        user_list = item.strip().split(':')
        if us.strip() == user_list[0] and pwd.strip() == user_list[1]:
            print("登陆成功")
            balance = int(user_list[2])
#            print(balance)
            print("           商品名称 商品价格")
#展示商品信息
            for k,v in comm_dict.items():
                msg = '''
              %s  %s
                '''%(k,v)
                print(msg)
            print("请根据商品名称选择购买商品")
            flag1 = True
            while flag1:
                usel = input('>>请输入商品名称：')
                if usel.strip() in comm_dict.keys():
#当用户余额大于要购买商品信息时，允许购买
                    if balance >= int(comm_dict[usel]):
                        print(usel+"购买成功")
                        balance = balance - int(comm_dict[usel])
                        print("余额："+str(balance))
#当用户余额小于购买商品信息时，继续循环商品信息供用户选择
                    else:
                        print("用户余额不足，请选择其他商品或充值后再购买此商品")
                        continue
#                        flag = False
#                        break
                elif usel == 'q':
                    flag = False
                    print("退出购物商城".center(50,'*'))
                    break
#将用户账号与余额定入文件
            user_list[2] = str(balance)
            str = ':'.join(user_list)
            list.append(str)
            str2 = '\n'.join(list)
            user_file1 = open('user','w+')
            user_file1.write(str2)
            user_file1.close()
    if flag == False:
        break
