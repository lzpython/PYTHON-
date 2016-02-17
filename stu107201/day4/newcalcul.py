__author__ = 'lizheng'
# !/usr/bin/env python
#-*- coding:utf-8 -*-

import re
#处理乘除
def mul_div(arg):
    #这里需要传入1个arg列表
    #对字符串进行乘除匹配,匹配从左至右最近的两个数字的乘除
    md = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',arg[0])
    #没匹配到就直接返回
    if not md:
        return arg
    #将匹配到的内容保存在content中
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',arg[0]).group()
    #对匹配到的内容进行计算
    if len(content.split('*'))>1:
        n1,n2 = content.split('*')
        computere = float(n1) * float(n2)
    else:
        n1,n2 = content.split('/')
        computere = float(n1) / float(n2)


    #取出匹配内容两头的内容：before，after
    before,after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',arg[0],1)
    #然后拼接成新的字符串
    new_str = "%s%s%s" %(before,computere,after)
    arg[0] = new_str
    #再递归进行乘除计算

    mul_div(arg)



#处理加减
def add_sub(arg):
    while True:
        if arg[0].__contains__('--') or arg[0].__contains__('+-') or arg[0].__contains__('--') or arg[0].__contains__('-+'):
            arg[0] = arg[0].replace('--','+')
            arg[0] = arg[0].replace('+-','-')
            arg[0] = arg[0].replace('-+','-')
            arg[0] = arg[0].replace('--','+')
        else:
            break
    #然后对传进来的arg[0]表达式进行第2次处理，提取首位为“-”，并将提取的次数保存在arg[1]中
    #并且没提取1次：将表达式中的"+"替换成"-"."-"替换成"+"，然后取arg[0]表达式字符串中第1到最后1位即可赋给arg[0]
    if arg[0].startswith('-'):
        arg[1]+=1
    #将arg[0]的第一位转换为‘+’
        arg[0] = arg[0].replace('-','%')
        arg[0] = arg[0].replace('+','-')
        arg[0] = arg[0].replace('%','+')
        arg[0] = arg[0][1:]
#对字符串进行匹配，匹配从左至右最近的两个数字的加减
    ad = re.search('\d+\.*\d*[\+\-]\d+\.*\d*',arg[0])
        #如果没匹配到就直接发回
    if not ad:
        return arg
    content = re.search('\d+\.*\d*[\+\-]\d+\.*\d*',arg[0]).group()
    #对匹配的内容进行加减计算
    if len(content.split('+'))>1:
         n1,n2 =content.split('+')
         computere = float(n1)+float(n2)
    else:
        n1,n2 =content.split('-')
        computere = float(n1)-float(n2)
    #取出匹配内容两头的内容，封装在before，after中
    before,after = re.split('\d+\.*\d*[\+\-]\d+\.*\d*',str(arg[0]),1)

    #将计算后的:before+结果+after，进行拼接，
    new_str = "%s%s%s" %(before, computere, after)
    #递归进行计算
    arg[0] = new_str
    add_sub(arg)


def compute(expr):
    #列表的第一个元素表示：待处理表达式，第二个元素代表提取的次数
    my_list = [expr,0]
     #先进行乘除运算
    mul_div(my_list)
    #再进行加减运算
    add_sub(my_list)

    #判断inp[1]是奇数还是偶数，若是奇数，表明结果为负数，否则为正数
    count = divmod(my_list[1],2)
    rr = float(my_list[0])
    if count[1] == 1:
        rr = rr * (-1)
    return rr

#去除括号表达式
def dropbrackets(expr):
    #匹配最里层的括号
    #若没括号直接返回表达式
    dd = re.search('\(([\+\-\*\/]*\d+\.*\d*){1,}\)',expr)
    if not dd:
        return expr

    #取出最里边括号的表达式
    content = re.search('\(([\+\-\*\/]*\d+\.*\d*){1,}\)',expr).group()
    new_content = content[1:len(content)-1]
    ##将expr按匹配的内容进行分割：得到--before,匹配内容，after,得到content两侧的内容，并赋值给before，after
    new_list = re.split('\(([\+\-\*\/]*\d+\.*\d*){1,}\)',expr,1)
    before = new_list[0]
    after = new_list[2]
    #将new_content进行计算，计算得到result
    cc = compute(new_content)
    #将括号内内容的计算结果（已经去掉括号）与未处理的表达式字符串拼接起来
    new_expr = "%s%s%s" %(before,cc,after)
    #递归执行dropbrackets(new_expr)，最终去掉所有的括号
    return dropbrackets(new_expr)

#主函数
if __name__ == "__main__":
    while True:
        str1 = input('>>请输入要计算的表达式，格式如：6*9-10*(3*2-1*9/3)+10；如果要退出，请输入q\n>>')
        #计算括号内内容，并生成无括号的表达式
        if str1 == 'q':
            break
        else:
            str2 = dropbrackets(str1)
            result = compute(str2)
            print("计算结果为:%s"%result)

