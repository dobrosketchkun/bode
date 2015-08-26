# -*- coding: utf-8 -*-
import random
import codecs
import hashlib
import ast

class WrongOption(Exception):
    pass

class BadHash(Exception):
    pass

test =  '''Alas, my love, you do me wrong,

To cast me off discourteously.

For I have loved you well and long,

Delighting in your company.'''

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

#Генерация ключа из файла
def dict_file(file):
    """создаёт из текстового файла словарь-ключ"""
    filee = codecs.open(file,"r","utf-8")
    file_lines = filee.read()
    d_k = dict_key(file_lines)
    return(d_k)
#########################################################################

#d_key = dict_file('text2.txt')


#########################################################################
def true_rand_choice(seq, file_rand='randorg.txt'):

    """даёт истинно случайный выбор из листа, используя файл с истинно случайными числами randorg.txt"""


    file = codecs.open(file_rand,"r","utf-8")
    file_lines = file.read()
    true_rand_list = file_lines.split(', ')

    t_r = int(random.choice(true_rand_list))
    #print(k)

    l_s = len(seq)
    #print("l_s =",l_s)

    while True:
        if t_r < l_s:
            return(t_r)
           # print("t_r =",t_r)
            break
        if t_r > l_s:
            f = t_r%l_s
           # print("f =",f)
            return(f)
            break

#########################################################################
def true_rand_coding(text='', file_t ='', file_rand='randorg.txt'):
    """кодирует текст на основе заранее созданного словаря-ключа, используя истинно случайные числа"""
    #открываем файл с рандомом из http://www.random.org/integer-sets/
    file = codecs.open(file_rand,"r","utf-8")
    file_lines = file.read()
    rand_list = file_lines.split(',')
    #d_key = dict_file(file_t)
    try:
        file = codecs.open(file,"r","utf-8")
        text = file_lines = file.read()
    except:
        text = text

    coded=[]
    for letter in text:
        if letter in d_key.keys():
            s = d_key[letter]
            #print(s)
            #часть, где мы истинно случайно выбираем кодовую цифру
            index= true_rand_choice(s,file_rand)
            choice = s[index]
            #print(choice)
            coded.append(choice)
        else:
            break
    return(coded)

#coded = true_rand_coding(test)

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

def doItwithCoded(coded, option, file_c = 'coded.txt',d_key = d_key): #добавил д_кей по умолчанию, для теста
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
            #print('sha512 from file =  ',sha512)
            #print('sha512 from dict =  ',hashlib.sha512(str(list(d_key.items())).encode('utf-8')).hexdigest())
            if sha512 == str(hashlib.sha512(str(list(d_key.items())).encode('utf-8')).hexdigest()):

                #print(coded_r)
                coded_r = [int(v) for v in coded_raw2[:-1]]
                #print(coded_r)
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
#print(coded)
#print(decoding(coded))
#doItwithCoded(coded, 'write')
#doItwithCoded(coded, 'read')