# -*- coding: utf-8 -*-

import argparse
import codecs
import sys
sys.path.append("C:/Python32/portable_python/pys/Bode") #для тестирования
import func_checkv2 as bd
import textwrap

parser = argparse.ArgumentParser(prog='Bode',    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\


                        Чтобы закодировать текствой файл имеющимся ключом
                             и сохранить его на диске, необходимо:

         -c (или --coding) путь_до_текстового_файла    путь_до_ключа   куда_сохранять

            ##########################################################################

                        Чтобы сгенерировать ключи из файла-источника:

            -k (или --keygen) путь_до_файла_источника   куда_сохранять_ключ

            ##########################################################################

                        Чтобы раскодировать файл при помощи ключи:
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


    d_key = bd.doItWithKey(key_file, 'read')
    coded = bd.true_rand_coding(file_t = source_file)
    bd.doItwithCoded(coded, 'write', file_c = coded_txt)

if args.keygen: #тут мы генерируем из источника файла-источника словарь-ключ и записываем его в файл
    key_source = args.keygen[0]
    key_file = args.keygen[1]


    d_key = bd.dict_file(key_source)
    bd.doItWithKey(key_file, 'write', d_key)


if args.decoding: #тут мы декодируем закодированный файл при помощи ключа и сохраняем текст
    coded_file = args.decoding[0]
    key_file = args.decoding[1]
    text_file = args.decoding[2]

    coded = bd.doItwithCoded([],'read',coded_file)
    d_key = bd.doItWithKey(key_file, 'read')
    decoded = bd.decoding(coded, d_key)
    bd.save_to_file(text_file, decoded)


#----------------------------------------------------------------------

#ДОДЕЛАТЬ

#----------------------------------------------------------------------
