# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        BoDe
# Purpose:     en/decrypt
#
# Author:      Wisketchy Dobrov
#
# Copyright:   (c)2013
# Licence:     The BSD 3-Clause License
#-------------------------------------------------------------------------------

import random
import codecs
import hashlib
import ast
import argparse
import textwrap


class WrongOption(Exception):
    pass

class BadHash(Exception):
    pass

#########################################################################
#########################################################################

def dict_key(text):
    """генерирует словарь-ключ из текста"""
    l = list(enumerate(text, start = 1))
    a = dict(l)

    b = {}
    for c in a.items():
      for d in c[1]:
        if d in b.keys():
          b[d].append(c[0])
        else:
          b[d] = [c[0]]

    return(b)

#########################################################################
#########################################################################

#Генерация ключа из файла
def dict_file(file):
    """создаёт из текстового файла словарь-ключ"""
    filee = codecs.open(file,"r","utf-8")
    file_lines = filee.read()
    d_k = dict_key(file_lines)
    return(d_k)

#########################################################################
#########################################################################

def true_rand_choice(seq, file_rand='randorg.txt'):

    """даёт истинно случайный выбор из листа, используя файл с истинно случайными числами randorg.txt"""


    file = codecs.open(file_rand,"r","utf-8")
    file_lines = file.read()
    true_rand_list = file_lines.split(', ')
    t_r = int(random.choice(true_rand_list))
    l_s = len(seq)


    while True:
        if t_r < l_s:
            return(t_r)
            break
        if t_r > l_s:
            f = t_r%l_s
            return(f)
            break

#########################################################################
#########################################################################

def true_rand_coding(file_t ='', file_rand='randorg.txt'): #Удалил "text=''," в начале аргументов, для теста
    """кодирует текст на основе заранее созданного словаря-ключа, используя истинно случайные числа"""
    #открываем файл с рандомом из http://www.random.org/integer-sets/
    try:
        file = codecs.open(file_rand,"r","utf-8")
        file_lines = file.read()
        rand_list = file_lines.split(',')

        try:
            file = codecs.open(file_t,"r","utf-8")
            text = file_lines = file.read()
            print(text)

            coded=[]
            for letter in text:
                if letter in d_key.keys():
                    s = d_key[letter]

                    #часть, где мы истинно случайно выбираем кодовую цифру
                    index= true_rand_choice(s,file_rand)
                    choice = s[index]

                    coded.append(choice)
                else:
                    break
            return(coded)
        except:
            print('Use text file, Luke')
    except IOError:
        print('''Use true randoms from http://www.random.org/integer-sets/ or another source, Luke.\
 It is should be a text file named "randorg.txt" with numbers by comma inside in bode.py directory.''' )



#########################################################################

def decoding(coded, d_key):

    """декодирует закодированный текст"""
    s=''

    for x in coded:
        for items in d_key:
            if x in d_key.get(items):
                s += ' '.join(items)

    return(s)

#########################################################################

def doItWithKey(file,option,d_k = []):


    try:
        if option == 'write':
            items = list(d_k.items()) #Делаем лист из кортежей, вида [(key, [values]), etc]
            items.append(('sha512: ', hashlib.sha512(str(list(d_k.items())).encode('utf-8')).hexdigest())) #добавляем sha512 от листа кортежей элементов словаря-ключа в конец листа в виде кортежа, для подписи файла
            items_s = str(items)
            open(file, 'w').write(items_s)

        elif option == 'read':
            filee = codecs.open(file,"r","utf-8").read()

            d_key = dict(ast.literal_eval(filee)[:-1]) #Эта команда, как я понял, передаёт строку именно так как она есть (что и нужно для чтения листа кортежей из файла)
            #так же мы учитываем, что мы добавили sha512 в конец листа в виде кортежа, убираем

            return(d_key)
        else:
            raise WrongOption
    except WrongOption:
        print(option, " ← Нет такого варианта option. Только write и read")
#########################################################################

def doItwithCoded(coded, option, file_c = 'coded.txt'):
    try:
        if option == 'write':
            coded_str = str(coded)[:-1] +', ' + hashlib.sha512(str(list(d_key.items())).encode('utf-8')).hexdigest() +']'
            open(file_c, 'w').write(coded_str)
        elif option == 'read':
            filee = codecs.open(file_c,"r","utf-8").read()

            coded_raw1 = filee[1:-1] #обрезаем []
            coded_raw2 = coded_raw1.split(',') #разбиваем в лист по запятым
            sha512 = str(coded_raw2[-1]) #забираем хэш
            sha512 = sha512[1:] #удаляем пробел


            if sha512 == str(hashlib.sha512(str(list(d_key.items())).encode('utf-8')).hexdigest()):
                coded_r = [int(v) for v in coded_raw2[:-1]]
                return(coded_r)
            else:
                raise BadHash

        else:
            raise WrongOption
    except WrongOption:
            print(option, " ← Нет такого варианта option. Только write и read")
    except BadHash:
            print("Хэши ключа, которым вы пытаетесь воспользоваться и которым был зашифрован файл не совпадают")


def save_to_file(file, decoded):
    open(file, 'w').write(decoded)

#########################################################################


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!





parser = argparse.ArgumentParser(prog='Bode',    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\


                        Чтобы сгенерировать ключи из файла-источника:

            -k (или --keygen) путь_до_файла_источника   куда_сохранять_ключ

            ##########################################################################


                        Чтобы закодировать текствой файл имеющимся ключом
                             и сохранить его на диске, необходимо:

         -c (или --coding) путь_до_текстового_файла    путь_до_ключа   куда_сохранять

            ##########################################################################


                        Чтобы раскодировать файл при помощи ключа:

            -d (или --decoding) путь_до_закодированного_файла   путь_до_ключа    куда_сохранять

            ##########################################################################
    '''))

parser.add_argument("-k", "--keygen", help="генерирует ключ и файла-источника",
                    dest="keygen", nargs = 2)
parser.add_argument("-c", "--coding", dest="coding",
                      help="кодирует текстовой файл по ключу и сохраняет его", nargs = 3)

parser.add_argument("-d", "--decoding", dest="decoding",
                      help="декодирует текстовой файл по ключу и сохраняет его", nargs = 3)


args = parser.parse_args()
if args.coding: #это всё работает, если есть файл, который нужно закодировать, ключ и куда это сохранять, именно в этом порядке
    #забираем аргументы по отдельности
    source_file = args.coding[0]
    key_file = args.coding[1]
    coded_txt = args.coding[2]


    d_key = doItWithKey(key_file, 'read')

    coded = true_rand_coding(file_t = source_file)

    doItwithCoded(coded, 'write', file_c = coded_txt)

if args.keygen: #тут мы генерируем из источника файла-источника словарь-ключ и записываем его в файл
    key_source = args.keygen[0]
    key_file = args.keygen[1]


    d_key = dict_file(key_source)
    doItWithKey(key_file, 'write', d_key)


if args.decoding: #тут мы декодируем закодированный файл при помощи ключа и сохраняем текст
    coded_file = args.decoding[0]
    key_file = args.decoding[1]
    text_file = args.decoding[2]

    d_key = doItWithKey(key_file, 'read')
    coded = doItwithCoded([],'read',coded_file)

    decoded = decoding(coded, d_key)
    save_to_file(text_file, decoded)



