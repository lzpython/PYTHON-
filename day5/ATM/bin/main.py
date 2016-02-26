__author__ = 'lizheng'
# !/usr/bin/env python
#-*- coding:utf-8 -*-
import os,sys,json
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
print(sys.path)
from account import checkaccount
from conf import setting
from bin import func
def run(isatm):
    count=0
    flag1 = True
    while flag1:
        if count<3:
            cardid_input = input('请输入卡号：>>')
            pwd_input = input('请输入密码：>>')
            temp_list = checkaccount.acc_check(cardid_input,pwd_input)
            acc_data = temp_list[0]
            acc_data_flag = temp_list[1]
            print(isatm)
            if acc_data_flag == 0 and isatm == 0:
                str = '''
                    ------- 中国银行 ---------
                    1.  账户信息(功能已实现)
                    2.  还款(功能已实现)
                    3.  取款(功能已实现)
                    4.  转账(功能已实现)
                    5.  账单
                    6.  退出(功能已实现)
                    '''
                str_dic = {
                        '1': func.accinfo,
                        '2': func.deposit,
                        '3': func.draw,
                        '4': func.transfer,
                        '6': func.logout
                }
                flag = True
                while flag:
                    print(str)
                    user_select = input(">>").strip()
                    if user_select in str_dic:
                        if user_select == '3':
                            str_dic[user_select](acc_data,isatm)
                            flag1 = False
                            break
                        else:
                            str_dic[user_select](acc_data)
                            if acc_data['status'] == -1:
                                flag1 = False
                                flag = False
            elif acc_data_flag == 0 and isatm != 0:
                str = '''
                    3.  充值(功能已实现)
                    '''
                str_dic = {
                        '3': func.draw,
                }
                flag = True
                while flag:
                    print(str)
                    user_select = input(">>").strip()
                    if user_select in str_dic:
                        if user_select == '3':
                            str_dic[user_select](acc_data,isatm)
                            flag1 = False
                            break
                        else:
                            str_dic[user_select](acc_data)
                            if acc_data['status'] == -1:
                                flag1 = False
                                flag = False
            elif acc_data_flag == 1:
                count+=1
            elif acc_data_flag == 2:
                flag1 = False
        else:
            db_path = setting.database["path"]
            acc_file = "%s\%s.txt" %(db_path,acc_data["id"])
            print('%s已经锁定'%cardid_input)
            acc_data["status"] = 1
            f = open(acc_file,'w')
            json.dump(acc_data,f)
            break


