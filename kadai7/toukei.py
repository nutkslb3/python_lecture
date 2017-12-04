#!/usr/bin/env python
# -*- coding:utf-8 -*-

from statistics import mean, variance, stdev

class Statman:

    def q8(self, sum11, sum12):
        m = []
        m1 = mean(sum11)
        var1 = variance(sum11)
        std1 = stdev(sum11)

        m2 = mean(sum12)
        var2 = variance(sum12)
        std2 = stdev(sum12)

        ##print("1-1の合計得点の平均:{0}".format(m1))
        ##print("1-1の合計得点の分散:{0}".format(var1))
        ##print("1-1の合計得点の標準偏差:{0}".format(std1))

        ##print("1-2の合計得点の平均:{0}".format(m2))
        ##print("1-2の合計得点の分散:{0}".format(var2))
        ##print("1-2の合計得点の標準偏差:{0}".format(std2))
        
        m.append(format(m1))
        m.append(format(var1))
        m.append(format(std1))

        m.append(format(m2))
        m.append(format(var2))
        m.append(format(std2))
        return (m)


    def q9(self, sum):
        ans = []
        m = mean(sum)
        var = variance(sum)
        std = stdev(sum)

        print("学年全体の合計得点の平均:{0}".format(m))
        print("学年全体の合計得点の分散:{0}".format(var))
        print("学年全体の合計得点の標準偏差:{0}".format(std))

        
        
    def q10(self, summale, sumfemale):
        malem =mean(summale)
        malevar = variance(summale)
        malestd = stdev(summale)

        femalem =mean(sumfemale)
        femalevar = variance(sumfemale)
        femalestd = stdev(sumfemale)

        print("学年全体の男子の合計得点の平均:{0}".format(malem))
        print("学年全体の男子の合計得点の分散:{0}".format(malevar))
        print("学年全体の男子の合計得点の標準偏差:{0}".format(malestd))

        print("学年全体の女子の合計得点の平均:{0}".format(femalem))
        print("学年全体の女子の合計得点の分散:{0}".format(femalevar))
        print("学年全体の女子の合計得点の標準偏差:{0}".format(femalestd))

if __name__ == '__main__':
    stat = Statman()
    data1 = [100, 200, 300]
    data2 = [400, 500, 600]
    stat.q8(data1, data2)
