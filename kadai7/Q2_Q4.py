#!/usr/bin/env python
#-*- coding:utf-8 -*-
import csv
import sys
import re
import numpy as np

class Student(object):
    def __init__(self):
        self.student_id = None
        self.name = ""
        self.math = None
        self.japanese = None
        self.mf = ""

class Classroom(object):
    def __init__(self):
        self.grade = None
        self.class_id = None
        self.student_list = None
        self.teacher_name = ""
        self.teacher_fm = None

def read_csv(filename):
    students1 = []
    f = open(filename,'r')
    dataReader1 = csv.reader(f)
    header = next(dataReader1)
    teacher = next(dataReader1)
    for row in dataReader1:
        student = Student()
        student.student_id = row[0]
        student.name = row[1]
        student.math = row[2]
        student.japanese = row[3]
        student.mf = row[4]
        students1.append(student)
    f.close()

    classroom1 = Classroom()
    classroom1.student_list = students1
    classroom1.grade = filename[0:1]
    classroom1.class_id = filename[2:3]
    classroom1.teacher_name = teacher[1]
    classroom1.teacher_fm = teacher[4]
    return classroom1
 
class yomikomi:
    def get11Max(self):
        #1組のデータを読み込み
        classroom1 = read_csv("1-1.csv")

        #1組のデータ
        math1 = 0   #個人の数学得点
        jpn1 = 0    #個人の国語得点
        total1 = 0  #個人の合計得点
        maxm1 = 0   #数学の最高得点
        maxj1 = 0   #国語の最高得点
        maxs1 = 0   #合計の最高得点
        stum1 = []  #数学最高得点者
        stuj1 = []  #国語最高得点者
        stus1 = []  #合計最高得点者

        s1 = ""     #性別
        stu1 = ""   #生徒

        #学年男女別のデータ
        stuam = []    #学年全体男子の名簿リスト
        mathM = []    #男子の数学得点リスト
        jpnM = []     #男子の国語得点リスト
        totalM = []   #男子の合計得点リスト
        stumM = []    #男子の数学最高得点者
        stujM = []    #男子の国語最高得点者
        stusM = []    #男子の合計最高得点者

        mathm = 0     #各男子生徒の数学得点
        jpnm = 0      #各男子生徒の国語得点
        totalm = 0    #各男子生徒の合計得点
        maxMathM = 0  #男子の数学最高得点
        maxJpnM = 0   #男子の国語最高得点
        maxTotalM = 0 #男子の最高合計得点

        stuaf = []    #学年全体女子の名簿リスト
        mathF = []    #女子の数学得点リスト
        jpnF = []     #女子の国語得点リスト
        totalF = []   #女子の合計得点リスト
        stumF = []    #女子の数学最高得点者
        stujF = []    #女子の国語最高得点者
        stusF = []    #女子の最高合計得点者

        mathf = 0     #各女子生徒の数学得点
        jpnf = 0      #各女子生徒の国語得点
        totalf = 0    #各女子生徒の合計得点
        maxMathF = 0  #女子の数学最高得点  
        maxJpnF = 0   #女子の国語最高得点
        maxTotalF = 0 #女子の最高合計得点

    
        #1組の最高得点者導出
        for i in range(int(classroom1.student_list[19].student_id)):
            math1 = int(classroom1.student_list[i].math)
            jpn1 = int(classroom1.student_list[i].japanese)
            total1 = math1 + jpn1
            s1 = str(classroom1.student_list[i].mf)
            stu1 = str(classroom1.student_list[i].name)

            if s1 == "M":
                mathM.append(math1)
                jpnM.append(jpn1)
                totalM.append(total1)
                stuam.append(stu1)
            elif s1 == "F":
                mathF.append(math1)
                jpnF.append(jpn1)
                totalF.append(total1)
                stuaf.append(stu1)

            if maxm1 < math1 or maxm1 == math1:
                maxm1 = math1

            if maxj1 < jpn1 or maxj1 == jpn1:
                maxj1 = jpn1

            if maxs1 < total1 or maxs1 == total1:
                maxs1 = total1

        return maxs1

    def get12Max(self):
        classroom2 = read_csv("1-2.csv") #2組のデータを読み込み
       
        #2組のデータ
        math2 = 0   #個人の数学得点
        jpn2 = 0    #個人の国語得点
        total2 = 0  #個人の合計得点
        maxm2 = 0   #数学の最高得点
        maxj2 = 0   #国語の最高得点
        maxs2 = 0   #合計の最高得点
        stum2 = []  #数学最高得点者
        stuj2 = []  #国語最高得点者
        stus2 = []  #合計最高得点者

        s2 = ""     #性別
        stu2 = ""   #生徒

        #学年男女別のデータ
        stuam = []    #学年全体男子の名簿リスト
        mathM = []    #男子の数学得点リスト
        jpnM = []     #男子の国語得点リスト
        totalM = []   #男子の合計得点リスト
        stumM = []    #男子の数学最高得点者
        stujM = []    #男子の国語最高得点者
        stusM = []    #男子の合計最高得点者

        mathm = 0     #各男子生徒の数学得点
        jpnm = 0      #各男子生徒の国語得点
        totalm = 0    #各男子生徒の合計得点
        maxMathM = 0  #男子の数学最高得点
        maxJpnM = 0   #男子の国語最高得点
        maxTotalM = 0 #男子の最高合計得点

        stuaf = []    #学年全体女子の名簿リスト
        mathF = []    #女子の数学得点リスト
        jpnF = []     #女子の国語得点リスト
        totalF = []   #女子の合計得点リスト
        stumF = []    #女子の数学最高得点者
        stujF = []    #女子の国語最高得点者
        stusF = []    #女子の最高合計得点者

        mathf = 0     #各女子生徒の数学得点
        jpnf = 0      #各女子生徒の国語得点
        totalf = 0    #各女子生徒の合計得点
        maxMathF = 0  #女子の数学最高得点  
        maxJpnF = 0   #女子の国語最高得点
        maxTotalF = 0 #女子の最高合計得点



        #2組の最高得点者導出
        for i in range(int(classroom2.student_list[17].student_id)):
            math2 = int(classroom2.student_list[i].math)
            jpn2 = int(classroom2.student_list[i].japanese)
            total2 = math2 + jpn2
            s2 = str(classroom2.student_list[i].mf)
            stu2 = str(classroom2.student_list[i].name)

            if s2 == "M":
                mathM.append(math2)
                jpnM.append(jpn2)
                totalM.append(total2)
                stuam.append(stu2)
            elif s2 == "F":
                mathF.append(math2)
                jpnF.append(jpn2)
                totalF.append(total2)
                stuaf.append(stu2)

            if maxm2 < math2 or maxm2 == math2:
                maxm2 = math2

            if maxj2 < jpn2 or maxj2 == jpn2:
                maxj2 = jpn2

            if maxs2 < total2 or maxs2 == total2:
                maxs2 = total2

        for j in range(int(classroom2.student_list[17].student_id)):
            math2 = int(classroom2.student_list[j].math)
            jpn2 = int(classroom2.student_list[j].japanese)
            total2 = math2 + jpn2

            if math2 == maxm2:
                stum2.append(classroom2.student_list[j].name)

            if jpn2 == maxj2:
                stuj2.append(classroom2.student_list[j].name)

            if total2 == maxs2:
                stus2.append(classroom2.student_list[j].name)

        return maxs2 
 
if  __name__ == '__main__':
    main()
