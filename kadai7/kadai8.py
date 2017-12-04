#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv
import toukei
import numpy as np
import Q2_Q4
import sort
import MeCab
import codecs
import re

m = MeCab.Tagger("/usr/lib/mecab/dic/mecab-ipadic-neologd")

class Student(object):

    def __init__(self):
        self.student_id = None
        self.name = None
        self.math = None
        self.japanese = None
        self.fm = None

class Classroom(object):

    def __init__(self):
        self.grade = None
        self.class_id = None
        self.student_list = None
        self.teacher_name = None
        self.teacher_fm = None

def read_csv(filename):
    students1 = []
    f = open(filename,"r")##ファイルを開く
    dataReader1 = csv.reader(f)##データの読み込み
    header = next(dataReader1)##一行目の読み込み
    teacher = next (dataReader1)##教師データの読み込み
    for row in dataReader1:
        student = Student()
        student.student_id = row[0]##生徒の名簿番号
        student.name = row[1]##生徒の名前
        student.math = row[2]##数学の点数
        student.japanese = row[3]##国語の点数
        student.fm = row[4]##性別
        students1.append(student)
    f.close()
    classroom1 = Classroom()
    classroom1.student_list = students1
    classroom1.grade = filename[0:1]##学年
    classroom1.class_id = filename[2:3]##クラス番号
    classroom1.teacher_name = teacher[1]##担任の名前
    classroom1.teacher_fm = teacher[4]##担任の性別
    return classroom1

class Teacher():

    def __init__(self):
        self.name1 = None
        self.class1 = None
        self.subject1 = None
        self.mail1 = None
        self.pmail1 = None
        self.phone1 = None
        self.url1 = None
        self.pr1 = None 
       
        self.name2 = None
        self.class2 = None
        self.subject2 = None
        self.mail2 = None
        self.phone2 = None
        self.url2 = None
        self.pr2 = None

    def mio(self):
        fin = codecs.open("./mio.txt", "r", "utf-8")
        mioprof = fin.read()
        fin.close()
        mailpat = "[A-Za-z0-9\._+-]+@[A-Za-z]+\.[A-Za-z\.]+"
        phonepat = r"([+-]?[0-9]+\.?[0-9]*)"
        urlpat = r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)"
        num = 0
        for line in mioprof.split("\n"):
            if num == 1:
                self.name1 = line
            if num == 3:
                self.class1 = line
            if num == 5:
                self.subject1 = line
            if num == 11:
                self.pr1 = line
            mail = re.findall(mailpat, line)
            phone = re.findall(phonepat, line)
            url = re.search(urlpat, line)
            if mail:
                self.mail1 = mail[0]
                self.pmail1 = mail[1]
            if phone:
                self.phone1 = phone
            if url:
                self.url1 = url.group(0)
            num += 1
   
    
    def taro(self):
        fin = codecs.open("./taro.txt", "r", "utf-8")
        taroprof = fin.read()
        fin.close() 
        mailpat = "[A-Za-z0-9\._+-]+@[A-Za-z]+\.[A-Za-z\.]+"
        phonepat = r"([+-]?[0-9]+\.?[0-9]*)" 
        urlpat = r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)"
        num = 0
        for line in taroprof.split("\n"):
            if num == 1:
                self.name2 = line
            if num == 3:
                self.class2 = line
            if num == 5:
                self.subject2 = line
            if num == 11:
                self.pr2 = line
            mail = re.search(mailpat, line)
            phone = re.findall(phonepat, line)
            url = re.search(urlpat, line)
            if mail:
                self.mail2 = mail.group(0)
            if phone:
                self.phone2 = phone
            if url:
                self.url2 = url.group(0)
            self.node2 = m.parseToNode(line)
            num += 1

def main():
    classroom1=read_csv("1-1.csv")
    classroom2=read_csv("1-2.csv")
    kadai7_q5 = sort.sortman() 
    kadai7_q8 = toukei.Statman() 
    ##１組の各生徒の数学国語の合計点数のリストの制作
    stum1=[]##学年全体の男子合計点リスト
    stuf1=[]##学年全体の女子合計点リスト
    sum11 =[]
    math1 = 0
    jpn1 = 0
    for i in range(int(classroom1.student_list[19].student_id)):
        math1 = int(classroom1.student_list[i].math)
        jpn1 = int(classroom1.student_list[i].japanese)
        sum11.append(math1 + jpn1)
        s1 = str(classroom1.student_list[i].fm)
        if (s1=="M"):
            stum1.append(math1 + jpn1)
        elif (s1=="F"):
            stuf1.append(math1 + jpn1)    
    ##２組の各生徒の数学国語の合計点数のリストの制作
    sum12 = []
    math2 = 0
    jpn2 = 0
    for i in range(int(classroom2.student_list[17].student_id)):
        math2 = int(classroom2.student_list[i].math)
        jpn2 = int(classroom2.student_list[i].japanese)
        sum12.append(math2 + jpn2)
        s2 = str(classroom2.student_list[i].fm)
        if (s2=="M"):
            stum1.append(math2 + jpn2)
        elif (s2=="F"):
            stuf1.append(math2 + jpn2)       
    ##学年全体の数学国語の合計点数のリストの制作
    sum1 =sum11 + sum12
    
    ##問５から問７まで
    #print ("")
    #kadai7_q5.q5(sum11,sum12)
    #print ("")
    #kadai7_q5.q6(sum1)
    #print ("")
    #kadai7_q5.q7(stum1,stuf1)
    
    ##問8から問１０まで
    #print ("")
    #kadai7_q8.q8(sum11,sum12)
    #print ("")
    #kadai7_q8.q9(sum1)
    #print ("")
    #kadai7_q8.q10(stum1,stuf1)
        
    ##教師インスタンスの生成
    teacher = Teacher()
    teacher.mio()
    teacher.taro()
 
    ##問題2
    q2 = toukei.Statman()
    mean11 = q2.get11Mean(sum11)
    mean12 = q2.get12Mean(sum12)

    if mean11 > mean12:
        print(teacher.name1 + "先生のクラスの勝ち")
    elif mean11 < mean12:
        print(teacher.name2 + "先生のクラスの勝ち")
    else:
        print(引き分け)
   
    ##問題3
    q3 = Q2_Q4.yomikomi()
    max11 = q3.get11Max()
    max12 = q3.get12Max()

    if max11 > max12:
        print(teacher.name1 + "先生のクラスの勝ち")
    elif max11 < max12:
        print(teacher.name2 + "先生のクラスの勝ち")
    else:
        print(引き分け)

    ##問題4
    print("名前：" + teacher.name1 + ", クラス：" + teacher.class1 + ", 担当教科：" + teacher.subject1)
    print("名前：" + teacher.name2 + ", クラス：" + teacher.class2 + ", 担当教科：" + teacher.subject2)


    ##問題5
    print(teacher.name1 + "先生のメールアドレス：" + teacher.mail1)
    print(teacher.name1 + "先生の個人アドレス：" + teacher.pmail1)
    print(teacher.name2 + "先生のメールアドレス：" + teacher.mail2)

    ##問題6
    print(teacher.name1 + "先生の携帯電話番号：" + teacher.phone1[1]+teacher.phone1[2]+teacher.phone1[3])
    print(teacher.name2 + "先生の携帯電話番号：" + teacher.phone2[1])

    ##問題7
    print(teacher.name1 + "先生の教師ページURL：" + teacher.url1)
    print(teacher.name2 + "先生の教師ページURL：" + teacher.url2)

    ##問題8
    print(teacher.name1 + "先生のプロフィール解析結果")
    print(m.parse(teacher.pr1))
    print(teacher.name2 + "先生のプロフィール解析結果")
    print(m.parse(teacher.pr2))

    ##問題9

    fin = codecs.open("./mio.txt", "r", "utf-8")
    for line in fin:
        node = m.parseToNode(line)

        while node:
            if node.feature.split(',')[0] != '名詞' and node.feature.split(',')[0] != '動詞':
                print(node.surface)
            node = node.next
    fin.close()


    fin = codecs.open("./taro.txt", "r", "utf-8")
    for line in fin:
        node = m.parseToNode(line)

        while node:
            if node.feature.split(',')[0] != '名詞' and node.feature.split(',')[0] != '動詞':
                print(node.surface)
            node = node.next
    fin.close()

   
if __name__ == '__main__':
    main() 
