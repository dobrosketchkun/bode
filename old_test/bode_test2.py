# -*- coding: utf-8 -*-
import random
import codecs
import hashlib
import ast

class WrongOption(Exception):
    pass

#---------------------------------------------------------------
# HASH TESTING
test =  '''Alas, my love, you do me wrong,

To cast me off discourteously.

For I have loved you well and long,

Delighting in your company.'''

##m = hashlib.md5()
##m.update(test.encode('utf-8'))
##print('md5: ',m.hexdigest())
##
##s512 = hashlib.sha512()
##s512.update(test.encode('utf-8'))
##print('sha512: ',s512.hexdigest())

#---------------------------------------------------------------

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




d_k = dict_file('text2.txt')

#########################################################################
def dict_gen_key_lister(d_k,option,file):
    items = list(d_k.items()) #Делаем лист из кортежей, вида [(key, [values]), etc]

    try:
        if option == 'write':
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

def true_rand_choice(seq, file_rand='randorg.txt'):

    """даёт истинно случайный выбор из листа, используя файл с истинно случайными числами randorg.txt"""


    file = codecs.open(file_rand,"r","utf-8")
    file_lines = file.read()
    true_rand_list = file_lines.split(', ')

    t_r = int(random.choice(true_rand_list))
    #print(k)

    l_s = len(seq)
    print("l_s =",l_s)

    while True:
        if t_r < l_s:
            return(t_r)
            print("t_r =",t_r)
            break
        if t_r > l_s:
            f = t_r%l_s
            print("f =",f)
            return(f)
            break

#########################################################################
def true_rand_coding(text, file_t ='text.txt', file_rand='randorg.txt'):
    """кодирует текст на основе заранее созданного словаря-ключа, используя истинно случайные числа"""
    #открываем файл с рандомом из http://www.random.org/integer-sets/
    file = codecs.open(file_rand,"r","utf-8")
    file_lines = file.read()
    rand_list = file_lines.split(',')
    #d_key = dict_file(file_t)

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

#########################################################################
def decoding(coded,file_t = 'text2.txt'):
#def decoding(coded, d_key, file_t = 'text2.txt'):
    coded = true_rand_coding(test)

    print(coded)
    """декодирует закодированный текс"""
    s=''
    d_key = dict_file(file_t)
    #print(d_key)
    ###d_key = dict_gen_key_lister(d_k,'read','ttt.txt')
    for x in coded:
        #print(x)
        for items in d_key.items():
            #print(items)

            #if x in d_key.get(items):
                print (d_key[x])
                s += ' '.join(items)
                print(s)

#____________________________________________________________________________________________________________________________________________
#Непонятки с этим циклом, надо что-то подумать, перебрать варианты с http://www.tutorialspoint.com/python/python_dictionary.htm
#____________________________________________________________________________________________________________________________________________
    return(s)
#########################################################################





#########################################################################
#####################    TEST AREA    ###################################
#########################################################################
if __name__ == '__main__':

    #dict_gen_key_lister(d_k,'write','ttt.txt')
    #d_key = dict_gen_key_lister(d_k,'read','ttt.txt')
    coded = true_rand_coding(test)
    #print('D_key: ', d_key)
    print('D_k: ', d_k)
    #decoding(coded)
    print('Coded: ',coded)
    #print("Decoded: ", decoding(coded, d_k))


##    fnamelst = ['ttt.txt']
##
##    print([(fname, hashlib.sha512(open(fname, 'rb').read()).hexdigest()) for fname in fnamelst])
##    print((hashlib.sha512(open('ttt.txt', 'rb').read())).hexdigest())
##
##    s512 = hashlib.sha512()
##    s512.update(str(list(d_k.items())).encode('utf-8'))
##    print('sha512: ',s512.hexdigest())
##
##
##
##    s512 = hashlib.sha512(str(list(d_k.items())).encode('utf-8')).hexdigest()
##    print('sha512: ', s512)