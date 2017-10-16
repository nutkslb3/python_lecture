#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys


def main():
    fruits = ["apple", "orange", "lemon", "strawberry", "apple", "cherry", "melon", "apple", "lemon"]
    print (fruits[::-1])

    fruits_converse = []
    for items in fruits:
        fruits_converse.append(items[::-1])    
    print (fruits_converse)

    counted_dict = {}
    for item in fruits:
        if item not in counted_dict:
             counted_dict[item] = 0
        counted_dict[item] += 1
    print (counted_dict)

    counted_length = {}
    for item in fruits:
             counted_length[item] = len(item)
    print (counted_length)
    print (sorted(counted_length.items(), key = lambda x:-x[1]))  	

if __name__ == '__main__':
    main()



