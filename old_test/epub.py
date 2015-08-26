# -*- coding: utf-8 -*-

import zipfile as z
import os
import codecs



path1 = '.\\test\\' #куда разархивируем
paths1 = [] #заготовка для списка необходимых файлов
zip1 = '1.epub'

zfile = z.ZipFile(zip1, "r")
#zip_path = os.path.abspath("1.epub")

for name in zfile.namelist():
    if '.xhtml' in name:
        data = zfile.read(name)
        print(name)
        zfile.extract(name, path1)
        paths1.append(path1+name)

#print(paths1)

for i in range(len(paths1)):
    paths1[i] = paths1[i].replace("/","\\")

#print(paths1)

l1 = []
l2 = []

for i in paths1:
    filee = codecs.open(i,"r","utf-8")
    file_lines = filee.read()
    #print (file_lines)
    l1.append(list(file_lines)) #запихиваем символы файлов в листы (по количеству файлов)

for lists in l1:
    for items in lists:
        l2.append(items) #объединяем все элементы листов в один большой

print(len(l2))




