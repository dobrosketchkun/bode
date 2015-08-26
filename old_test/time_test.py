#!/usr/bin/env python
import time
import random
import codecs
import math

#открываем файл с рандомом и строим лист
file = codecs.open('randorg.txt',"r","utf-8")
file_lines = file.read()
b = file_lines.split(',')


s = [12, 50, 58, 104, 125, 159, 170, 207, 211, 232, 262, 293, 298, 327, 348, 364, 370, 428, 455, 487, 492, 522, 629, 738, 755, 796, 860, 932, 972, 978, 998, 1015, 1074, 1104, 1114, 1118, 1137, 1258, 1295, 1373, 1417]

first = []
second = []

ran = 50

for i in range(ran):
    start1 = time.time()

    k = int(random.choice(b))


    t = len(s)
    for i in range(1000000):
        while True:
            p = k/t
            p = p/t
            if p / t < t:
                f = int(math.modf(p)[1])
                break
        continue

    first.append((time.time() - start1))


    start2 = time.time()

    k = int(random.choice(b))





    t = len(s)
    for i in range(1000000):
        while True:
            p = k/t
            p = p/t
            if p / t < t:
                f = int(p)
                break
        continue
    second.append(time.time() - start2)


first = sum(first)/ran
second = sum(second)/ran

if first>second:
    proc = second/first * 100
if second>=first:
    proc = first/second * 100

print(str(proc) + "%")