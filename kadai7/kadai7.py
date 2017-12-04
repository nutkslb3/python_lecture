#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv
import toukei
import numpy as np
import Q2_Q4
import sort
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

class readFile:
    def read_csv(self,filename):
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
    
def main():
    read = readFile()
    classroom11=read.read_csv("1-1.csv")
    classroom12=read.read_csv("1-2.csv")
    kadai7_q2 = Q2_Q4.yomikomi()
    kadai7_q2.q2()
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
    print ("")
    kadai7_q5.q5(sum11,sum12)
    print ("")
    kadai7_q5.q6(sum1)
    print ("")
    kadai7_q5.q7(stum1,stuf1)
    ##問8から問１０まで
    print ("")
    kadai7_q8.q8(sum11,sum12)
    print ("")
    kadai7_q8.q9(sum1)
    print ("")
    kadai7_q8.q10(stum1,stuf1)
if __name__ == '__main__':
    main()

