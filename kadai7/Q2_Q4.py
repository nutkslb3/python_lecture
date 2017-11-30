#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Q2Q4:
    
    def get_max(self, classroom):
        math_order = sorted(classroom.student_list, reverse=True, key=lambda x: x.math)
        jap_order = sorted(classroom.student_list, reverse=True, key=lambda x: x.japanese)
        tot_order = sorted(classroom.student_list, reverse=True, key=lambda x: x.total)

        return({"math":math_order, "japanese":jap_order, "total":tot_order})
        
    def get_max_grade(self, grade):
        math_order = sorted(grade, reverse=True, key=lambda x: x.math)
        jap_order = sorted(grade, reverse=True, key=lambda x: x.japanese)
        tot_order = sorted(grade, reverse=True, key=lambda x: x.total)
        
        return({"math":math_order, "japanese":jap_order, "total":tot_order})
        
    def get_MF(self, grade):
        M_grade = []
        F_grade = []
        for g in grade:        
            if g.fm == "M":
                M_grade.append(g)
            else:
                F_grade.append(g)
        
        math_order_m = sorted(M_grade, reverse=True, key=lambda x: x.math)
        jap_order_m = sorted(M_grade, reverse=True, key=lambda x: x.japanese)
        tot_order_m = sorted(M_grade, reverse=True, key=lambda x: x.total)
        
        math_order_f = sorted(F_grade, reverse=True, key=lambda x: x.math)
        jap_order_f = sorted(F_grade, reverse=True, key=lambda x: x.japanese)
        tot_order_f = sorted(F_grade, reverse=True, key=lambda x: x.total)

        return([{"math":math_order_m, "japanese":jap_order_m, "total":tot_order_m}
               ,{"math":math_order_f, "japanese":jap_order_f, "total":tot_order_f}])


if  __name__ == '__main__':
    main()
