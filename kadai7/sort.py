#!/usr/bin/env python
# -*- coding:utf-8 -*-


class sortman: 

    def q5(self, classroom):
        students = classroom.student_list
        students.sort(reverse=True, key=lambda x: x.total)
        
        return(students)

    def q6(self, classroom1, classroom2):
        students = []
        students.extend(classroom1.student_list)
        students.extend(classroom2.student_list)
        students.sort(reverse=True, key=lambda x: x.total)
        
        return(students)

    def q7(self, classroom1, classroom2):
        student_m = []
        student_f = []
        for student in classroom1.student_list:
            if student.fm == "M":
                student_m.append(student)
            else:
                student_f.append(student)

        for student in classroom2.student_list:
            if student.fm == "M":
                student_m.append(student)
            else:
                student_f.append(student)

        
        student_m.sort(reverse=True, key=lambda x: x.total)
        student_f.sort(reverse=True, key=lambda x: x.total)
        
        return([student_m, student_f])
 
