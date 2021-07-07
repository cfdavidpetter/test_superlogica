'''
Seed of Units

This is a script to create an excel spreadsheet with false data,
and be pasted into the Superlogica System Units Register.
'''

import os
import csv
import pathlib
import faker

# header of CSV with all fields for insertion.
header = [
    'unidade', 
    'bloco', 
    'fracao', 
    'area',
    'abatimento',
    'proprietario_nome',
    'proprietario_telefone',
    'proprietario_celular',
    'proprietario_forma_de_entrega',
    'proprietario_cpf/cnpj',
    'proprietario_rg',
    'proprietario_email',
    'proprietario_endereco',
    'proprietario_complemento',
    'proprietario_cep',
    'proprietario_cidade',
    'proprietario_bairro',
    'proprietario_estado',
    'inquilino_nome',
    'inquilino_telefone',
    'inquilino_celular',
    'inquilino_forma_de_entrega',
    'inquilino_cpf/cnpj',
    'inquilino_rg',
    'inquilino_email',
    'inquilino_endereco',
    'inquilino_complemento',
    'inquilino_cep',
    'inquilino_cidade',
    'inquilino_bairro',
    'inquilino_estado'
]

# body of CSV.
fake = faker.Faker(['pt_BR'])
data = []
for x in range(0, 100):
    data.append([
        (x + 1),
        '',
        '',
        fake.random_int(min=60, max=600),
        '',
        fake.name(), 
        f'(11) {fake.random_int(min=3000, max=3999)}-{fake.random_int(min=9000, max=9999)}',
        f'(11) 9{fake.random_int(min=9000, max=9999)}-{fake.random_int(min=9000, max=9999)}',
        fake.random_int(min=0, max=3),
        fake.cpf(),
        fake.rg(),
        fake.email(),
        fake.street_address(),
        '',
        fake.postcode(formatted=False),
        fake.city(),
        fake.bairro(),
        fake.random_int(min=1, max=27),
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
    ])

# name file
path_name = pathlib.Path(__file__).parent.resolve()
file_name = os.path.join(path_name, 'files', 'create_csv_units_and_owner.csv')

# making file
with open(file_name, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=';')

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)