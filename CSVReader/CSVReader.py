import csv
import sys
from Fileutilities.absolutepath import absolutepath


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []

        try:
            file = open(absolutepath(filepath))
        except OSError:
            print("Could not open/read file:", filepath)
            sys.exit()

        with file:
            csv_data = csv.DictReader(file, delimiter=',')
            for row in csv_data:
                self.data.append(row)


    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects
