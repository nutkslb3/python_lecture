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
        self.name = ""
        self.math = 0
        self.japanese = 0
        self.total = 0
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
        student.math = int(row[2])  ##数学の点数
        student.japanese = int(row[3])##国語の点数
        student.total = student.math + student.japanese
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
    classroom1=read_csv("1-1.csv")
    classroom2=read_csv("1-2.csv")

    Q2 = Q2_Q4.Q2Q4()

    # １組の最高得点
    class1_max = Q2.get_max(classroom1)
    print("1組の最高点")
    print_Q2(class1_max)
    
    # ２組の最高得点
    class2_max = Q2.get_max(classroom2)
    print("2組の最高点")
    print_Q2(class2_max)

    # 全体の最高得点
    class1_max["total"].extend(class2_max["total"])
    grade_max = Q2.get_max_grade(class1_max["total"])
    print("全体の最高点")
    print_Q2(grade_max)

    #学年全体の男女別の最高点
    grade_max_list = Q2.get_MF(class1_max["total"])
    print("男子の最高点", end='\n')
    print_Q2(grade_max_list[0])
    print("女子の最高点", end='\n')
    print_Q2(grade_max_list[1])

    '''
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
'''

def print_Q2(class_max):
    print("数学" + str(class_max["math"][0].math) + "点：", end='')
    for i, n in enumerate(class_max["math"]):
        if n.math == class_max["math"][0].math:
            print(n.name + "さん　", end='')
    print("")

    print("国語" + str(class_max["japanese"][0].japanese) + "点：", end='')
    for i, n in enumerate(class_max["japanese"]):
        if n.japanese == class_max["japanese"][0].japanese:
            print(n.name + "さん　", end='')
    print("")

    print("合計" + str(class_max["total"][0].total) + "点：", end='')
    for i, n in enumerate(class_max["total"]):
        if n.total == class_max["total"][0].total:
            print(n.name + "さん　", end='')
    print("\n")


if __name__ == '__main__':
    main()

