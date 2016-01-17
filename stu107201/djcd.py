__author__ = 'thinkpad'
flag1 = True
#循环选择第一级菜单
while flag1:
    print('1.北京\n2.湖北')
    sel1 = input('>>请选择:')
    flag2 = True
#进入第一级菜单未
    if sel1 == 'q':
        break
    elif sel1 == 'b':
       continue
    elif sel1 == '1':
#循环选择第二级菜单
      while flag2:
        flag3 = True
        print('--1.东城\n--2.昌平')
        if sel1 == '1':
           flag4 = True
#循环选择第三级菜单
           while flag3:
              sel2 = input('>>请再次选择:')
              if sel2 == '1':
                print('----1.安定门街道\n----2.建国门街道')
                flag4 = False
              elif sel2 == '2':
                print('----1.小汤山镇\n----2.阳坊镇')
                flag4 = False
              elif sel2 == 'q':
                flag1 = False
                flag2 = False
                flag3 = False
#进入第二级菜单时退出到第一级
              elif sel2 == 'b' and flag4 == True:
                flag3 = False
                flag2 = False
#进入第三级菜单时退出到第二级
              elif sel2 == 'b' and flag4 == False:
#               flag2 = True
                flag4 = True
                flag3 = False
              else:
                  continue
        elif sel1 == 'b':
           flag2 = False
        elif sel1 == 'q':
           flag1 = False
        else:
            continue
#当用户输入的不是列出的项或不是退出及回退时，继续循环让用户选择
    else:
        continue


    
