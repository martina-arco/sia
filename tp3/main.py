# from GeneticAlgorithm import GeneticAlgorithm
# from GeneticFunctionsImplementation import GeneticFunctionsImplementation
import csv


def read_file(file_name, array):
    with open(file_name) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            array.append(row)


if __name__ == "__main__":

    weapons = []
    boots = []
    helmets = []
    gloves = []
    shirts = []

    read_file('testdata/armas.tsv', weapons)
    read_file('testdata/botas.tsv', boots)
    read_file('testdata/cascos.tsv', helmets)
    read_file('testdata/guantes.tsv', gloves)
    read_file('testdata/pecheras.tsv', shirts)

    print(weapons[0]['Fu'])

