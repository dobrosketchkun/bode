# -*- coding: utf-8 -*-

##text = 'hello world'
##unique_letters = set(text)
##analize = {}
##for letter in unique_letters:
##    analize[letter] = text.count(letter)
##
##print(analize) # => {' ': 1, 'e': 1, 'd': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1})
##

import random
import codecs
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

def save_to_file(file,text):
    """сохраняет текст в файл"""
    with open(file, mode='wt', encoding='utf-8') as myfile:
        myfile.write("".join(text))

#########################################################################

#Генерация ключа из файла
def dict_file(file):
    """создаёт из текстового файла словарь-ключ"""
    filee = codecs.open(file,"r","utf-8")
    file_lines = filee.read()
    d_k = dict_key(file_lines)
    return(d_k)


###запись словаря-ключа в текстовой файл. Потом подумать как читать из него
##with open ('wvtc_data.txt', 'w') as fp:
##    for p in d_k.items():
##        fp.write("%s:%s\n" % p)


#d_key = dict_file('text.txt') #генерация словаря-ключа из файла text.txt

test =  '''Alas, my love, you do me wrong,

To cast me off discourteously.

For I have loved you well and long,

Delighting in your company.'''

#########################################################################

def coding(text, file_t='text.txt'):
    """кодирует текст на основе заранее созданного словаря-ключа"""
    coded=[]
    d_key = dict_file(file_t)
    for letter in text:
        if letter in d_key.keys():
            s = d_key[letter]
            d = random.choice(s)
            coded.append(d)
        else:
            break
    return(coded)

#coded = coding(test, 'text.txt') #кодировка и получение листа

#t = d_key.values()

#print(t)
##for items in coded:
##    if items in d_key:
##
####    if items in d_key.values():
##        print(dict.get(key))
##    else:
##        print('Error')




##for item in list(d_key.keys()):
##    for x in coded:
##        if x in d_key.get(item):
##            print(item)

#########################################################################

def decoding(coded, file_t='text.txt'):
    coded = coding(test, file_t)
    """декодирует закодированный текс"""
    s=''
    d_key = dict_file(file_t)
    for x in coded:
        for items in d_key:
            if x in d_key.get(items):
                s += ' '.join(items)

    return(s)

#########################################################################


def true_rand_choice(seq, file_rand='randorg.txt'):

    """даёт истинно случайный выбор из листа, используя файл с истинно случайными числами randorg.txt"""


    file = codecs.open(file_rand,"r","utf-8")
    file_lines = file.read()
    true_rand_list = file_lines.split(', ')

    t_r = int(random.choice(true_rand_list))
    #print(k)

    l_s = len(seq)
    #print("t =",l_s)

    while True:
        if t_r < l_s:
            return(t_r)
            #print("t_r =",t_r)
            break
        if t_r > l_s:
            f = t_r%l_s
            #print("f =",f)
            return(f)
            break

#########################################################################

def true_rand_coding(text, file_t ='text.txt', file_rand='randorg.txt'):
    """кодирует текст на основе заранее созданного словаря-ключа, используя истинно случайные числа"""
    #открываем файл с рандомом из http://www.random.org/integer-sets/
    file = codecs.open(file_rand,"r","utf-8")
    file_lines = file.read()
    rand_list = file_lines.split(',')
    d_key = dict_file(file_t)

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



#Тестирование, если не модуль
if __name__ == '__main__':
    #print("d_key - ",d_key)
    print("")
    #print("coded1 - ",coded)
    print("")
    #print("decoding1 - ",decoding(coded))
    coded2 = true_rand_coding(test)
    print('')
    print("coded2 -",coded2)
    print('')
    decoded = decoding(coded2)
    print('')
    print("decoding2 - ",decoded)