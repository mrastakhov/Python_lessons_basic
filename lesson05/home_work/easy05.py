# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
import sys
path_dir =[('dir_' + str(i + 1)) for  i in range(9)]

def make_dir(paths):
    path_dir = os.path.join(os.getcwd(),paths)
    try:
        os.mkdir(path_dir)
    except:
        print(path_dir + ' - такая директория уже есть')
for i in path_dir:
    make_dir(i)

def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()


def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)

main_path = os.getcwd()

list_dir(main_path)


def copy_file(first_file, backup_file):
    shutil.copy(first_file, backup_file)


# first_file = sys.argv[0]
# backup_file = first_file + '.backup'
# copy_file(first_file,backup_file)


def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - такой директории нет')


def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(dir_path + ' - такой директории нет')
