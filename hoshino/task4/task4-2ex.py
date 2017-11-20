#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import codecs
import csv

def main():
    try:
        fin = codecs.open("./data.csv", "rb", "utf-8")
        reader = csv.reader(fin)
        for row in reader:
            ",".join(row)  
    except IOError as e:
        print("ファイルが開けません")
        sys.exit()
    finally:
        fin.close()
    str  = row[0].split("-")
    N = int(str[0])
    L = int(str[1])
    ans = 1
    if N == 0:
        print(0)
        sys.exit()
    for i in range(1, N + 1):
        if L >= int(row[i]):
           L -= int(row[i])
        else:
            L = int(str[1])
            L -= int(row[i])
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
