'''
Seed of Consumption 

This is a script to create an excel spreadsheet with data to 
demonstrate the consumption of units.
'''

import os
import csv
import pathlib
import datetime
import faker

# menu
menu = 'What is the type of consumption?\n1 Gas\n2 Water\n3 Energy\n4 Mineral Water\nR: '
string = int(input(menu))

# header of CSV with all fields for insertion.
header = [
    'unidade', 
    'bloco', 
    'mes', 
    'ano', 
    'consumo', 
    'leitura', 
]

# body of CSV.
t = datetime.date.today()
fake = faker.Faker(['pt_BR'])
data = []
for x in range(0, 100):
    data.append([
        (x + 1),
        '',
        t.month,
        t.year,
        string,
        fake.random_int(min=10, max=200),
    ])

# name file
path_name = pathlib.Path(__file__).parent.resolve()
file_name = os.path.join(path_name, 'files', 'create_csv_to_import_the_consumption_of_unit.csv')

# making file
with open(file_name, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=';')

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)