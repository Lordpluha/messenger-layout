import os
from copy import *


list_of_fonts = []

i = 0

file_scss = '_fonts.scss'

path = os.getcwd()

with open(file_scss, 'w') as w_f:
    for dirs, folder, files in os.walk(path):
        print('Файлы: ', files)

        for el in files:
            file_split = os.path.splitext(el)
            file_folder = dirs.split('\\')
            print(file_folder)

            if file_split[1] == '.otf':
                print('Выделение расширения шрифта закончено!')

                w_f.write('@font-face {')
                text_for_print = ('   font-family: \' {0}\';').format(file_split[0])
                w_f.write(text_for_print)
                w_f.write(str('   font-style: normal;'))
                w_f.write(str('   font-weight: normal;'))

                text_for_print = ('   src: url({0}/{1}.otf) format(\'opentype\');').format(file_folder[-1], file_split[0])

                w_f.write(text_for_print)
                w_f.write('}')

                print('Сохранение .otf шрифта завершено')

            elif file_split[1] == '.ttf':
                print('Выделение расширения шрифта закончено!')

                w_f.write('@font-face {')
                text_for_print = ('   font-family: \' {0}\';').format(file_split[0])
                w_f.write(text_for_print)
                w_f.write(str('   font-style: normal;'))
                w_f.write(str('   font-weight: normal;'))

                text_for_print = ('   src: url({0}/{1}.ttf) format(\'truetype\');').format(file_folder[-1], file_split[0])

                w_f.write(text_for_print)
                w_f.write('}')

                print('Сохранение .ttf шрифта завершено')

            else:
                continue

with open(file_scss, 'r') as w_f:
    print('___', file_scss,'___')

    print('FINISHED')
    print('_______________________________')


print("Скрипт завершился удачно")
input()

"""

Использование скрипта:
 - Поместите скрипт в папку scss или css
 - Запустите
 - Подключите к проэкту _fonts.scss

 - Готово!
"""