import random
import codecs
import math

#открываем файл с рандомом и строим лист
file = codecs.open('randorg2.txt',"r","utf-8")
file_lines = file.read()
b = file_lines.split(', ')
##print(b)
##print(len(b))
##k = int(random.choice(b))
##print(k, type(k), k/k)

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


def dict_file(file):
    """создаёт из текстового файла словарь-ключ"""
    filee = codecs.open(file,"r","utf-8")
    file_lines = filee.read()
    d_k = dict_key(file_lines)
    return(d_k)



d_key = dict_file('text2.txt')

test = '''Alas, my love, you do me wrong,

To cast me off discourteously.

For I have loved you well and long,

Delighting in your company.'''

def coding(text):
    """кодирует текст на основе заранее созданного словаря-ключа"""
    coded=[]
    for letter in text:
        if letter in d_key.keys():
            s = d_key[letter]
            d = random.choice(s)
            coded.append(d)
        else:
            break
    return(coded)

coded = coding(test) #кодирование

def decoding(coded):
    """декодирует закодированный текс"""
    s=''
    for x in coded:
        for items in d_key:
            if x in d_key.get(items):
                s += ' '.join(items)

    return(s)

decoded = decoding(coded) #декодирование


##s = [12, 50, 58, 104, 125, 159, 170, 207, 211, 232, 262, 293, 298, 327, 348, 364, 370, 428, 455, 487, 492, 522, 629, 738, 755, 796, 860, 932, 972, 978, 998, 1015, 1074, 1104, 1114, 1118, 1137, 1258, 1295, 1373, 1417]
##
##d = random.choice(s)
##k = int(random.choice(b))
##
##print(k)
##
##t = len(s)
##print(t, len(s))


##while True:
##    p = k/t
##    p = p/t
##    if p / t < t:
##        f = int(math.modf(p)[1])
##        ff = int(p)
##        print(f, ff)
##        break

##while True:
##    p = k/t
##    p = p/t
##    if p / t < t:
##        f = int(p)
##        print(f)
##        break





def true_rand_choice(seq, file_rand='randorg2.txt'):

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

def true_rand_coding(text, file_rand='randorg2.txt'):
    """кодирует текст на основе заранее созданного словаря-ключа, используя истинно случайные числа"""
    #открываем файл с рандомом из http://www.random.org/integer-sets/
    file = codecs.open(file_rand,"r","utf-8")
    file_lines = file.read()
    rand_list = file_lines.split(',')


    coded=[]
    for letter in text:
        if letter in d_key.keys():
            s = d_key[letter]
            #print(s)
            #часть, где мы истинно случайно выбираем кодовую цифру
            index= true_rand_choice(s,file_rand)
            choice = s[index]
            print(choice)
            coded.append(choice)
        else:
            break
    return(coded)

coded2 = true_rand_coding(test)

#print(d_key)
#print(coded)
#print('')
print(coded2)
decoded = decoding(coded2)
print(test)
print(decoded)
