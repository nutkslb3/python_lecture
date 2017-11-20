#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys



args = sys.argv

V = args[1]
v = V.split(",")
## print(v[1]) こうすると二番目から出る
u = v[0].split("-")

count = 0 ##使った紐
N = int(u[0])  ##人数
L = int(u[1])  ##紐の長さ

i = 0
while i < N:
	l = int(v[i + 1]) ##ほしい紐の長さ
	if L > l:
		L = L - l
	if L < l:
		L = int(u[1]) - l
		count = count + 1
	i = i + 1 
print(count)  



	
