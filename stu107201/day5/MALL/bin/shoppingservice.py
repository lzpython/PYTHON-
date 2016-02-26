# !/usr/bin/env python
#-*- coding:utf-8 -*-

def run():
    import os,sys
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    from MALL.bin import recharge
    f = r"%s\db\user.txt" %base_dir
    user_file = open(f,'r+')
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
                balance = float(user_list[2])
                print("余额为%s"%balance)
                flag2 = True
                while flag2:
                    print("1.充值\n2.购物\n3.退出")
                    use2 = input('>>请选择类型：')
                    if use2 == '1':
                        use3 = input('>>请输入充值金额：')
                        balance = float(balance)+float(use3)
                        recharge.rech(use3)
                        print("余额%s"%balance)
                    elif use2 == '2':
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
                                if balance >= float(comm_dict[usel]):
                                    print(usel+"购买成功")
                                    balance = balance - float(comm_dict[usel])
                                    print("余额："+str(balance))
            #当用户余额小于购买商品信息时，继续循环商品信息供用户选择
                                else:
                                    print("用户余额不足，请选择其他商品或充值后再购买此商品")
                                    continue
            #                        flag = False
            #                        break
                            elif usel == 'q':
                                flag = False
                                flag2 = False
                                print("退出购物商城".center(50,'*'))
                                break
                    elif use2 == '3':
                        flag2 = False
    #将用户账号与余额定入文件
                user_list[2] = str(balance)
                str1 = ':'.join(user_list)
                list.append(str1)
                str2 = '\n'.join(list)
                user_file1 = open(f,'w+')
                user_file1.write(str2)
                user_file1.close()
        if flag == False:
            break

