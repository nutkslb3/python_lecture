#!/usr/bin/env python
# -*- coding:utf-8 -*-


def main():
    fruits = ["apple", "orange", "lemon", "strawberry", "apple", "cherry", "melon", "apple", "lemon"]
    print(fruits[::-1])
    
    fruits2 = []
    for item in fruits:
        fruits2.append(item[::-1])
    print(fruits2)
    
    fruits3 = {}
    for item in fruits:
        if not item in fruits3:
            fruits3[item] = 0
        fruits3[item] += 1
    print(fruits3)
    
    fruits4 = {}
    for item in fruits:
        fruits4[item] = len(item) 
    print(fruits4)

    fruits5 = {}
    for item in fruits:
        fruits5[item] = len(item)
    print(sorted(fruits5.items(), key=lambda x:x[1], reverse=True))
    

if __name__ == '__main__':
    main()
