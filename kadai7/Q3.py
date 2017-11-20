#!/usr/bin/env python
# -*- coding:utf-8 -*-


def q5(sum11, sum12):
    sum11.sort()

    sum11.reverse()

    sum12.sort()

    sum12.reverse()

    print('1組クラス別ソート' + str(sum11))

    print('2組クラス別ソート' + str(sum12))

def q6(sum):
    sum.sort()
    sum.reverse()
    
    print('学年ソート' + str(sum))

def q7(sum1,sum2):
    sum1.sort()
    sum1.reverse()

    sum2.sort()
    sum2.reverse()

    print('男子ソート' + str(sum1))
    print('女子ソート' + str(sum2))
if __name__ == '__main__':
    data1 = [122,121,123]
    data2 = [222,223,221]
    q5(data1, data2)
    q6(data1)
    q6(data2)
    q7(data1,data2)

 
