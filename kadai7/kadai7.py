#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv

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
    f = open(filename,"r")
    dataReader1 = csv.reader(f)
    header = next(dataReader1)
    teacher = next (dataReader1)
    for row in dataReader1:
        student = Student()
        student.student_id = row[0]
        student.name = row[1]
        student.math = row[2]
        student.japanese = row[3]
        student.fm = row[4]
        students1.append(student)
    f.close()
    classroom1 = Classroom()
    classroom1.student_list = students1
    classroom1.grade = filename[0:1]
    classroom1.class_id = filename[2:3]
    classroom1.teacher_name = teacher[1] 
    classroom1.teacher_fm = teacher[4]
    return classroom1

    
def main():
    classroom11=read_csv("1-1.csv")
    classroom12=read_csv("1-2.csv") 

if __name__ == '__main__':
    main()

