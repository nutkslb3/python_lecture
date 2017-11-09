#!/usr/bin/env python
# -*- coding:utf-8 -*-
import codecs

def main():
    fin = codecs.open("./data.txt","r","utf-8")
    lines2 = fin.readlines()
    fin.close()
    b=lines2[0].split("-")
    N = int(b[0])
    L = int(b[1])
    used = 1
    for i in range(1,N+1):
        if L>=int (lines2[i]):
            L-=int (lines2[i])
        else:
            L=int (b[1])
            L-=int (lines2[i])
            used += 1
    print (used)


if __name__ == '__main__':
        main()
