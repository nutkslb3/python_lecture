#!/usr/bin/env python
# -*- coding:utf-8 -*-
class sortman: 

    def q5(self,sum11, sum12):
        sum11.sort()

        sum11.reverse()

        sum12.sort()

        sum12.reverse()

        print('1組クラス別ソート' + str(sum11))

        print('2組クラス別ソート' + str(sum12))

    def q6(self,sum):
        sum.sort()
        sum.reverse()

        print('学年ソート' + str(sum))
	
    def q7(self,sum1,sum2):
        sum1.sort()
        sum1.reverse()

        sum2.sort()
        sum2.reverse()

        print('男子ソート' + str(sum1))
        print('女子ソート' + str(sum2))
