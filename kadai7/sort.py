#!/usr/bin/env python
# -*- coding:utf-8 -*-
class sortman: 

    def q8_q3(self,sum11, sum12):
        sum1 = []

        sum11.sort()

        sum11.reverse()

        sum12.sort()

        sum12.reverse()
       
        sum1.append (sum11[0])
        sum1.append (sum12[0])

        return sum1 

    def q5sum11(self,sum11):
        sum11 = []

        sum11.sort()

        sum11.reverse()
        
        return sum11

    def q5sum12(self,sum12):
        sum12 = []

        sum12.sort()

        sum12.reverse()

        return sum12    

    def q6(self,sum):
        sum.sort()
        sum.reverse()
        
        return sum 

    def q7(self,sum1,sum2):
        sum1.sort()
        sum1.reverse()

        sum2.sort()
        sum2.reverse()

        print('男子ソート' + str(sum1))
        print('女子ソート' + str(sum2))
