import pandas as pd
import csv
import re

def read_file_csv(library_origin,):
    data_csv = []
    with open(library_origin, "r") as read_file:
        temp_data = csv.reader(read_file, delimiter=',')
    
        for i in temp_data:
            data_csv.append(i)

    return data_csv

def numbers_rows(variable):
     print(len(variable))

def name_partner(data_csv):
    name_partner = []

    for data in data_csv:
        name_partner.append(data[0])

    return name_partner

def number_quotas(data_csv):
    quotas_str = []

    for data in data_csv:
        temp_quotas = data[5]
        quotas_str.append(*(re.findall(f"\d+",temp_quotas)))

    return quotas_str

def transform_int(number_quotas):
    quotas = []

    for data in number_quotas:
        temp = int(data)
        quotas.append(temp)

    return quotas

def create_dataframe(name_partner, quotas):
    partner_quotas = pd.DataFrame()

    partner_quotas["Partners"] = name_partner
    partner_quotas["Cotas"] = quotas

    return partner_quotas

def export_to_csv(file, library_dest):
    file.to_csv(library_dest)


library_origin = "../data_raw/Pasta2.csv"
library_dest = "../data_processed/database.csv"

print("******************* LOG ********************")

print("\nLendo o arquivo e atribuindo a uma variavel")
data = read_file_csv(library_origin)

print("\nExibindo a quantidade de registros importados")
numbers_rows(data)

print("\nAtribuindo nomes dos partners a uma variavel")
name = name_partner(data)

print("\nExibindo a quantidade de registros dos nomes atribuidos")
numbers_rows(name)

print("\ncapturando total de cotas em str")
quota_temp = number_quotas(data)

print("\ntransformando as cotas em números inteiros")
quota = transform_int(quota_temp)

print("\nExibindo a quantidade de registros de cotas")
numbers_rows(quota)

print("\nCriando Dataframe")
database = create_dataframe(name,quota)

print("\nExportando para o Excel")
export_to_csv(database,library_dest)


