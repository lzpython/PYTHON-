__author__ = 'lizheng'
# !/usr/bin/env python
#-*- coding:utf-8 -*-

import json,os

def getdict(ss):
    my_dict = json.loads(ss)
    return my_dict


#定义get函数，并同时传入我们指定backend的参数
def get(bk):
    flag = False #定义flag，目的是为了后面是否取可用的backend
    get_list=[]  #定义空列表，目的是为了后面将取出的backend信息存储在此列表里面
    #以读的形式打开'haproxy'文件,一行一行读，然后将我们指定backend的记录读取到列表里面
    with open('haproxy') as obj:
        for line in obj:
            if line.strip() == "backend %s" %(bk):
                flag = True
                continue
            if line.strip().startswith('backend'):
               flag=False
            if flag and line.strip():
                get_list.append(line.strip())

    return get_list

#定义add1函数，并同时传入参数input_dict
def add(input_dict):

    backend_content = input_dict['backend'] #要插入的backend的名称
    backend_all = "backend %s" %(backend_content)  #要插入backend整个字段
    record_content = input_dict["record"]
    #要插入的记录整个字段
    record_all = "server %s weight %s maxconn %s" %(record_content["server"],record_content["weight"],record_content["maxconn"])

    #将backend获取，并存储在get_list列表里面
    get_list=get(backend_content)

    #如果要插入的backend存在
            #flag:用于找到要添加的backend下的内容
            #flag_write:用于判断get_list中的内容是否重新写入到了文件

    if get_list:
        flag=False
        flag_write = False
        with open('haproxy') as read_obj,open('haproxy.new','w') as write_obj:
            for line in read_obj:
                if line.strip() == backend_all:
                    write_obj.write("\n"+line)
                    flag=True
                    flag_write=False
                    continue
                if flag and line.startswith('backend'):
                    flag = False
                if flag:
                    if not flag_write:
                        for item in get_list:
                            temp = "%s%s" %(" "*8,item+'\n')
                            write_obj.write(temp)
                            flag_write=True
                        temp1 = "%s%s" %(" "*8,record_all+'\n')
                        write_obj.write(temp1)
                else:
                    write_obj.write(line)


    else:
    #如果要插入的backend不存在
            # 从haproxy文件里面直接读取，并同时将读取的内容写入新的文件haproxy.new
            # 将新的信息直接写到新的文件haproxy.new的文件尾部
        with open('haproxy') as read_obj,open('haproxy.new','w') as write_obj:
            for line in read_obj:
                write_obj.write(line)
            write_obj.write("\n"+backend_all+"\n")
            temp=" "*8+record_all+"\n"
            write_obj.write(temp)

    print("%s 添加成功"%input_dict)
    os.rename('haproxy','haproxy.bak')
    os.rename('haproxy.new','haproxy')

def delete(input_dict):
    backend_content = input_dict['backend'] #要插入的backend的名称
    backend_all = "backend %s" %(backend_content)  #要插入backend整个字段
    record_content = input_dict["record"]
    #要插入的记录整个字段
    record_all = "server %s weight %s maxconn %s" %(record_content["server"],record_content["weight"],record_content["maxconn"])

    #将backend获取，并存储在get_list列表里面
    get_list=get(backend_content)

    if not get_list:
        return
    #判断2：否则不为空
    else:
        #判断1：若用户输入的server信息不在get_list里面，直接返回
        if record_all not in get_list:
            print("你要删除的内容不存在")
            return
        #判断2：若输入的server在_list里面，就将此server信息从列表中移除
        else:
            get_list.remove(record_all)
            # 判断其实就是我们自己输入的backend，找到后将列表get_list信息写入到新的文件里面。
            # 其余的非列表的内容直接从源文件haproxy写到新文件haproxy.new即可
        with open('haproxy','r') as read_obj,open('haproxy.new','w') as write_obj:
            flag = False
            flag_write = False
            for line in read_obj:
            #当要删除的记录原来大于一行时
                if get_list.__len__() > 0:
                    if line.strip() == backend_all:
                        write_obj.write(line)
                        flag = True
                        flag_write = False
                        continue
                    if flag and line.startswith('backend'):
                        flag = False
                        flag_write = False
                    if flag:
                          if not flag_write:
                            for item in get_list:
                                temp = "%s%s" %(" "*8,item+'\n')
                                write_obj.write(temp)
                                flag_write=True
                          continue
                    else:
                         write_obj.write(line)
            #当要删除的记录原来只有一行时，删除后要连同backend记录一起删除
                else:
                    if line.strip() == backend_all:
                        flag = True
                        flag_write = True
                        continue
                    if flag and line.startswith('backend'):
                        flag = False
                        flag_write = False
                    if flag:
                          if not flag_write:
                            for item in get_list:
                                temp = "%s%s" %(" "*8,item+'\n')
                                write_obj.write(temp)
                                flag_write=False
                          continue
                    else:
                         write_obj.write(line)
    print("%s 删除成功"%input_dict)
    os.rename('haproxy','haproxy.bak')
    os.rename('haproxy.new','haproxy')

#主函数
flag1 = True
while flag1:
    if __name__ == "__main__":
        print("1.查询\n2.增加\n3.删除\n4.退出\n")
        select_num=input("请选择操作类型（输入类型序号）:")

    #根据用户的选择，进行调用函数

        if select_num == "1":
            backend = input("请输入backend对应的值:")
            get_list = get(backend)
            for i in get_list:
                print(i)
        elif select_num == "2":
            print("输入例子如下:")
            print('{"backend":"ttt.oldboy.org","record":{"server":"100.1.7.9","weight":"20","maxconn":"3000"}}')
            input_str = input("请用户照以上例子输入内容>>>")
            data_dict = getdict(input_str)
            add(data_dict)
        elif select_num == "3":
            print("输入例子如下:")
            print('{"backend":"ttt.oldboy.org","record":{"server":"100.1.7.9","weight":"20","maxconn":"3000"}}')
            input_str = input("请用户照以上例子输入内容>>>")
            data_dict = getdict(input_str)
            delete(data_dict)
        elif select_num == '4':
            break
        else:
            print("输入有误")
