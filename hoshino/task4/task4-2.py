#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys

def main():
    args = sys.argv
    str = args[1].split(",")
    str2 = str[0].split("-")
    N = int(str2[0])
    L = int(str2[1])
    ans = 1
    if N == 0:
        print(0)
        sys.exit()
    for i in range(1, N + 1):
        if L >= int(str[i]):
           L -= int(str[i])
        else:
            L = int(str2[1])
            L -= int(str[i])
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
