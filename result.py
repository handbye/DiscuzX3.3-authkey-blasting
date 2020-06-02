# coding: utf-8
f = open("result.txt",'r')
f1 = open("result1.txt",'a+')
file = f.readlines()
for i in file:
    if "HHVM" in i:
        f1.write(i)

