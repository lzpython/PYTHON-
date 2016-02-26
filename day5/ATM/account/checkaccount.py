__author__ = 'lizheng'
# !/usr/bin/env python
#-*- coding:utf-8 -*-
import os,sys,json,time
dir_name1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_name1)
from conf import setting
def acc_check(cardid,pwd):
    db_path = setting.database["path"]
    acc_file = "%s\%s.txt" %(db_path,cardid)
    if os.path.exists(acc_file):
        with open(acc_file,'r') as f:
            user_dict = json.load(f)
            if user_dict["status"] == 0:
                if user_dict["passwd"] == pwd:
                    end_time_stamp = time.mktime(time.strptime(user_dict['end_date'], "%Y-%m-%d"))
                    if time.time() > end_time_stamp:
                        print("卡号为[%s]的卡已经过了有效期，请联系发卡银行更换新卡片" % cardid)
                    else:
                        my_list = [user_dict,0]
                        return  my_list
                else:
                    my_list = [user_dict,1]
                    print("%s的密码不正确"%cardid)
                    return  my_list
            else:
                print("%s已经被锁定"%cardid)
                my_list = [user_dict,2]
                return  my_list
    else:
        print("%s账号不存在"%cardid)
        return [{},0]

