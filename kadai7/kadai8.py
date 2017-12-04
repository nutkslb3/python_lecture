#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MeCab
import re
import Q2_Q4
import toukei
import kadai7
import sort

class Teacher(object):
    def __init__(self):
        self.name = None
        self.class_ = None
        self.subject = None
        self.mailaddress = None
        self.address = None
        self.profile = None
        self.url = None


def read_txt(filename):
    teacher = Teacher()
    f = open(filename,'r')
    data = f.readline()
    i = 0     
    while data:
        if (i==1):
            teacher.name=data
        if (i==3):
            teacher.class_=data
        if (i==5):
            teacher.subject=data
        if (i==7):
            teacher.mailaddress = data 
        if (i==9):
            teacher.address = data
        if (i==11):
            teacher.profile = data
        if (i==13):
            teacher.url =data
        i=i+1
        data = f.readline()
    f.close()
    return teacher

def main():
    mio = read_txt("mio.txt")
    taro = read_txt("taro.txt")
    q2() 
    print ("")
    print (mio.name)
    print (mio.class_)
    print (mio.subject)
    q5(mio.mailaddress)
    q6(mio.address)
    q7(mio.url)
    q8(mio.profile)
    q9("mio.txt")    
    print ("")   
    print (taro.name)
    print (taro.class_)
    print (taro.subject)
    q5(taro.mailaddress) 
    q6_t(taro.address)
    q7_t(taro.url)
    q8(taro.profile)
    q9("taro.txt")

def q2():
    read = kadai7.readFile()
    classroom1 = read.read_csv("1-1.csv")
    classroom2 = read.read_csv("1-2.csv")
    ##１組の各生徒の数学国語の合計点数のリストの制作
    sum11 =[]
    math1 = 0
    jpn1 = 0
    for i in range(int(classroom1.student_list[19].student_id)):
        math1 = int(classroom1.student_list[i].math)
        jpn1 = int(classroom1.student_list[i].japanese)
        sum11.append(math1 + jpn1)
    ##２組の各生徒の数学国語の合計点数のリストの制作
    sum12 = []
    math2 = 0
    jpn2 = 0
    for i in range(int(classroom2.student_list[17].student_id)):
        math2 = int(classroom2.student_list[i].math)
        jpn2 = int(classroom2.student_list[i].japanese)
        sum12.append(math2 + jpn2)

    ##問２
    print ("問２")
    toi2 = toukei.Statman()
    m = toi2.q8(sum11,sum12)
    if (m[0]>m[3]):
        print ("mio先生の勝ち")
    elif(m[3]>m[0]):
        print ("taro先生の勝ち") 

    ##問３
    print ("")
    print ("問３")
    toi3 = sort.sortman()
    n = toi3.q8_q3(sum11,sum12)
    if (n[0]>n[1]):
        print ("mio先生の勝ち")
    elif(n[1]>n[0]):
        print ("taro先生の勝ち")
 
def q5(mailaddress):
    m = re.findall("[A-Za-z-0-9-\._+]+@[A-Za-z]+\.[A-Za-z\.]+",mailaddress)      
    print(m)

def q6(address):
    m = re.search("[0-9]{4}",address)
    print (m.group(0))
    n = re.search("[0-9]{3}-[0-9]{4}-[0-9]{4}",address)
    print (n.group(0))    

def q6_t(address):
    m = re.search("[0-9]{4}",address)
    print (m.group(0))
    n = re.search("[0-9]{11}",address)
    print (n.group(0))

def q7(url):
    m = re.search("[http://[A-Za-z0-9\-.+]+/([A-Za-z0-9\-.+])+/([A-Za-z0-9\-.+])+/([A-Za-z0-9\-.+])+/",url)
    print (m.group(0))

def q7_t(url):
    m = re.search("[http://[A-Za-z0-9\-.+]+/([A-Za-z0-9\-.+])+/([A-Za-z0-9\-.+])+/([A-Za-z0-9\-.+])+/",url)
    print (m.group(0))
    n = re.search("[http://[A-Za-z0-9\-.+]+/([A-Za-z0-9\-.+])+/([A-Za-z0-9\-.+])+/([A-Za-z0-9\-.+])+/([A-Za-z0-9\-.+])+",url)
    print (n.group(0))

def q8(profile):
    m = MeCab.Tagger()
    m.parse('')
    print (m.parse(profile))
    node = m.parseToNode(profile)
    keywords = []
    while node:
        if node.feature.split(",")[0] == u"助詞":
            keywords.append(node.surface)
        elif node.feature.split(",")[0] == u"形容詞":
             keywords.append(node.surface)
        elif node.feature.split(",")[0] == u"副詞":
             keywords.append(node.surface)
        elif node.feature.split(",")[0] == u"助動詞":
             keywords.append(node.surface)
        elif node.feature.split(",")[0] == u"感動詞":
             keywords.append(node.surface)
        node = node.next
    print (keywords)
    
def q9(filename):
    m = MeCab.Tagger()
    f = open(filename,'r')
    for line in f:
        node = m.parseToNode(line)
        while node:
            if node.feature.split(',')[0] != '名詞' and node.feature.split(',')[0] != '動詞':
                print(node.surface)
            node = node.next
    f.close()

if __name__ == '__main__':
    main()


