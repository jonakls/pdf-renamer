import csv
import os

root_directory = os.getcwd()
files_directory = root_directory + str('\\files')
files_directory_renamed = root_directory + str('\\renamed')
csv_file = root_directory + str('\\read.csv')


def main():
    create_directories()
    files = os.listdir(files_directory)
    if len(files) == 0:
        print('Se necesitan archivos en la carpeta files')
        return
    with open(csv_file, newline='') as File:
        reader = csv.reader(File)
        print('Iniciando proceso con ' + str(reader.__sizeof__()) + ' valores en csv')
        for row in reader:
            evaluate_files(row, files)


def evaluate_files(csv_value, files):
    if len(csv_value) > 2:
        print('Los valores de el archivo csv no corresponden, por favor revisa')
        return
    if len(csv_value) < 1:
        print('Los valores de el archivo csv no corresponden, por favor revisa')
        return
    for file in files:
        if csv_value[0].__contains__(';'):
            if csv_value[0].split(';')[0] == file.split('.pdf')[0]:
                rename_file(file, csv_value[0].split(';')[1])
                return
        if csv_value[0].__contains__(','):
            if csv_value[0].split(',')[0] == file.split('.')[0]:
                rename_file(file, csv_value[0].split(',')[1])
                return


def rename_file(file, new_name):
    os.rename(files_directory + str('\\') + file, files_directory_renamed + str('\\') + new_name + str('.pdf'))
    print('Archivo ' + str(file) + ' renombrado a: ' + str(new_name))


def create_directories():
    if not os.path.exists(files_directory):
        os.mkdir(files_directory)
    if not os.path.exists(files_directory_renamed):
        os.mkdir(files_directory_renamed)
    if not os.path.exists(csv_file):
        print('Se necesita del archivo csv para iniciar')


main()
