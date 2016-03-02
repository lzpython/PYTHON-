__author__ = 'lizheng'
# !/usr/bin/env python
#-*- coding:utf-8 -*-
class person:
    school_name = None
    skills = 0
    job_status = None
    interviewer = None
    company = None

    def __init__(self, name,sex,level,company):
        self.name = name
        self.sex = sex
        self.level = level
        self.company = company
        if self.level == 'HR':
            print('\033[32;1mMy name is %s,I am a %s interviewer \033[0m'\
            %(self.name,self.company))
        elif self.level == 'ordinary':
            print('\033[32;1mMy name is %s,I just graduated from college,I\'m looking for a job,I went to the %s interview \033[0m' % \
            (self.name, self.company))
        elif self.level == 'senior':
            print('\033[32;1mMy name is %s, Through continuous learning, I have the ability to meet all of the requirements of %s company\033[0m' % (self.name,self.company))


    def say(self, msg, flag = 'toothers'):
        #默认对别人说话
        if flag == 'toothers':
            print('%s: %s' % (self.name, msg))
        #自言自语
        elif flag == 'tome':
            print('\033[31;1m%s: %s\033[0m' % (self.name, msg))

    def learning(self,status):
        if status == 'study':
            self.skills += 2000
            print('\033[32;1m%s is on the rise \033[0m' %self.name)



#故事章节
def Fragment(page):
    print('*****'+page+'*****')


p1 = person('lizheng', 'male', 'ordinary','HUAWEI')

Fragment('1: A growth story')

p2 = person('Merry', 'female', 'HR','HUAWEI')
p1.interviewer = p2
p1.job_status = 'nothing'
p1.say('Hello,%s,My name is %s,I would like to apply for your company\'s maintenance engineer, I graduated from XX university computer professional, proficient in Linux..... '%(p2.name,p1.name))
p2.say('Hello,%s,I\'m sorry!Your ability to reach our requirements'%p1.name)
p1.say('Never mind, continue to work hard to enhance their own ability, I can enter HUAWEI.','tome')


Fragment('2: Story development')
#不断学习，增加能力值，当能力值达到5000以上即达到面试华为要求
count = 0
skill_list = ['python','java','ocp']
while int(p1.skills)<5000:
    print('sdudying %s'%skill_list[count])
    p1.learning('study')
    p1.say('The capacity is not enough, I will continue to .','tome')水土第一
    count+=1
#    print(p1.skills)

print('My ability to meet the requirements, GO, goes to the interview!!! ')

Fragment('3: Story end')
tmp = p1.skills
p1 = person('lizheng', 'male', 'senior','HUAWEI')
p3 = person('Jim', 'male', 'HR','HUAWEI')
p1.interviewer = p3
p1.say('Hello,%s,My name is %s,I fully meet your company\'s requirements, is expected to be one of you,my skills is %s'%(p3.name,p1.name,tmp))
p2.say('Hello,%s,Welcome to join the %s company'%(p1.name,p1.company))
p1.say('I finally managed to enter the %s company.'%p1.company,'tome')
