__author__ = 'lizheng'
# !/usr/bin/env python
#-*- coding:utf-8 -*-
import os,sys,json
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
print(sys.path)
from conf import setting
def accinfo(account):
    msg = '''
        ************账号信息****************
        卡号：%s
        信用额度：%s
        可用额度：%s
        卡片有效期起：%s
        卡片有效期止：%s
        '''%(account['id'],account['total'],account['balance'],account['start_date'],account['end_date'])
    print(msg)

def logout(account):
    account['status'] = -1
    return account

def deposit(account):
    print('欠款为%s'%(float(account['total'])-float(account['balance'])))
    while True:
        deposit_money = input('请输入还款金额：')
        if float(deposit_money) > 0:
            account['balance'] = str(float(account['balance'])+float(deposit_money))
            if float(account['balance']) > float(account['total']):
                account['total'] = str(float(account['balance']))
        else:
            print("输入的金额不能为负数！！")
        print(account)
        db_path = setting.database["path"]
        acc_file = "%s\%s.txt" %(db_path,account["id"])
        f = open(acc_file,'w')
        json.dump(account,f)
        break

def draw(account,isatm):
    if isatm == 0:
        print('欠款为%s'%(float(account['total'])-float(account['balance'])))
        while True:
            draw_list =[]
            draw_money = input('请输入取款金额：')
            if float(draw_money) > 0:
                if float(float(draw_money)) <= float(account['balance']):
                    account['balance'] = str(float(account['balance'])-float(draw_money)*1.05)
                else:
                    print("取款金额不能大于账户余额！！")
            else:
                print("输入的金额不能为负数！！")
            print(account)
            draw_list.append(draw_money)
            db_path = setting.database["path"]
            db_path1 = setting.database["log"]
            acc_file = "%s\%s.txt" %(db_path,account["id"])
            log_file = "%s\%s.log" %(db_path1,account["id"])
            f = open(acc_file,'w')
            f1 = open(log_file,'w')
            json.dump(account,f)
            json.dump(draw_list,f1)
            f.close()
            f1.close()
            break
    else:
        while True:
            draw_money = isatm
            if float(draw_money) > 0:
                if float(float(draw_money)) <= float(account['balance']):
                    account['balance'] = str(float(account['balance'])-float(draw_money))
                    print("%s充值成功"%draw_money)
                else:
                    print("取款金额不能大于账户余额！！")
            else:
                print("输入的金额不能为负数！！")
            print(account)

            db_path = setting.database["path"]
            db_path1 = setting.database["log"]
            acc_file = "%s\%s.txt" %(db_path,account["id"])
            log_file = "%s\%s.log" %(db_path1,account["id"])
            f = open(acc_file,'w')
            f1 = open(log_file,'w')
            json.dump(account,f)
            f.close()
            f1.close()
            break
def transfer(account):
    totransfer_id = input('请输入要转入的账号:')
    totransfer_money = input('请输入要转入的金额:')
    db_path = setting.database["path"]
    acc_file1 = "%s\%s.txt" %(db_path,totransfer_id)
    acc_file2 = "%s\%s.txt" %(db_path,account["id"])
    if acc_file1:
        with open(acc_file1,'r') as f1:
            totransfer_dict = json.load(f1)
            account['balance'] = str(float(account['balance'])-float(totransfer_money))
            totransfer_dict['balance'] = str(float(totransfer_dict['balance'])+float(totransfer_money))
            f1 = open(acc_file1,'w')
            json.dump(totransfer_dict,f1)
        with open(acc_file2,'r') as f2:
             f2 = open(acc_file2,'w')
             json.dump(account,f2)
        print("转账成功！")
    else:
        print("您要转入的账号不存在，请核实后再输入！！")