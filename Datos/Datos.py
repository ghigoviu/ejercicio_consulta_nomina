import csv


class Datos:
    def all_data(self, csv_doc):
        datos = []
        with open(csv_doc, encoding='latin-1') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                datos.append(row)
        file.close()
        return datos
