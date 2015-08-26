import codecs
def true_rand_coding(file_t ='', file_rand=''): #Удалил "text=''," в начале аргументов, для теста
    """кодирует текст на основе заранее созданного словаря-ключа, используя истинно случайные числа"""
    #открываем файл с рандомом из http://www.random.org/integer-sets/

    #d_key = dict_file(file_t)

    file = codecs.open(file_t,"r","utf-8")
    text = file_lines = file.read()
    print(text)

    print('lala')

true_rand_coding(file_t='123.txt')

