
# -*- coding:utf-8 -*-
import csv
import numpy as np
import Q2_Q3
import re
import MeCab
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


class Teacher(object):

    def __init__(self):
        self.room = None
        self.name = None
        self.subject = None
        self.mail = None
        self.pmail = None
        self.url = None
        self.telephone = None

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
    
def read_txt(filename):
    teacher = Teacher()
    f1 = open(filename,"r")
    line = f1.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f1.close()# line :リスト。要素は1行の文字列データ
    teacher.name = line[1]
    teacher.room = line[3]
    teacher.subject = line[5]
    teacher.mail = line[7]
    teacher.telephone = line[9]
    teacher.profile = line[11]
    teacher.url = line[13]
    return teacher

def main():
    classroom1=read_csv("1-1.csv")
    classroom2=read_csv("1-2.csv")
    teacher1 = read_txt("mio.txt")
    teacher2 = read_txt("taro.txt")
    kadai8_q3 = Q2_Q3.question2()
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
    ##課題８問２から問３まで
    
    kadai8_q3.q2(sum11,sum12)
    
    kadai8_q3.q3(sum11,sum12)

    ##課題８の問４
    name1 = teacher1.name
    room1 = teacher1.room
    subject1 = teacher1.subject
    name2 = teacher2.name
    room2 = teacher2.room
    subject2 = teacher2.subject
    print("先生の名前  " + name1)
    print(name1 + "先生の担任  " + room1)
    print(name1 + "先生の担当  " + subject1)
    print("先生の名前  " + name2)
    print(name2 + "先生の担任  " + room2)
    print(name2 + "先生の担当  " + subject2)
    ##課題８の問５
    mail1 = teacher1.mail
    m1 = q5(mail1)
    print(m1)
    mail2 = teacher2.mail
    m2 = q5(mail2)
    print(m2)
    ##課題８の問６
    phone1 = teacher1.telephone
    p1 =  q6(phone1)
    print(p1)
    phone2 = teacher2.telephone
    p2 = q6(phone2)
    print(p2)
    ##課題８の問７
    url1 = teacher1.url
    u1 = q7(url1)
    print(u1)
    url2 = teacher2.url
    u2 = q7(url2)
    print(u2)
    ##課題8の問８
    profile1 = teacher1.profile
    kekka = q8(profile1)
    print(kekka)
    profile2 = teacher2.profile
    keka = q8(profile2)
    print(keka)
    ##課題8の問９
    habu = q9('mio.txt')
    for w in habu:
        print(w)
    habuku = q9('taro.txt')
    for i in habuku:
        print(i)

##課題８の問５
def q5(add):
    m = re.findall('[a-z]+\@[A-Za-z]+\.[a-zA-Z\.]+', add)
    return m
##課題8の問６
def q6(phone):
    p = re.findall('[0-9]{3}-?[0-9]{4}-?[0-9]{4}', phone)
    return p
##課題8の問７
def q7(url):
    u = re.findall('[a-z]{4}:/{2}[a-z\.\/]+',url)
    return u

##課題８の問8
def q8(profile):
    t = MeCab.Tagger('-Owakati')
    kekka = t.parse(profile)
    return kekka

##課題８の問９
def q9(text):
    t = MeCab.Tagger()
    txt = open(text,'r')
    keyword = []
    for line in txt:
        node = t.parseToNode(line)
        while node:
            if node.feature.split(',')[0] != '名詞' and node.feature.split(',')[0] != '動詞':
                keyword.append(node.surface)
            node = node.next
    txt.close()
    return keyword
if __name__ == '__main__':
    main()    
