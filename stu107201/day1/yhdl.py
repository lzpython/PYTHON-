#首先定义锁文件，用于存储锁定账号
lockfr = open('lock','r+')
lockfr_line = lockfr.readlines()
us = input('请输入用户名:').strip()
lock_list = []
#锁定账号转换为列表
for item in lockfr_line:
     line = item.strip('\n')
     lock_list.append(line)
#用户首次登陆查找锁定表，如果存在即退出；
if us in lock_list:
     print(us,'已经被锁定,请联系管理员.退出!')
else:
#用户名如果不在锁定表中，即与用户表比对，当三次比对失败即退出循环
     count = 0
     while count < 3:
            count = count + 1
            username = us
            passwd = input('请输入密码:').strip()
            userfr = open('user', 'r')
            userfr_line = userfr.readlines()
            login = False
            for line in userfr_line:
                if username == line.split(":")[0] and passwd == line.split(":")[1].strip():
                    print("欢迎登录系统")
                    login = True
#当用户输入密码正确时跳出for循环
                    break
                else:
#当用户密码不正确时，继续while循环
                    continue
#当用户输入密码正确时跳出while循环并退出程序
            if login is True:
                 break
#当输入次数超出3次时执行下面的文件写操作
     else:
        lockfr.write(us)
        lockfr.write('\n')
        lockfr.close()
        print(us,'你的密码输入超过三,锁定帐号,退出')