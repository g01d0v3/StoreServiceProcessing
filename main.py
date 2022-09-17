import sqlalchemy
from sqlalchemy import MetaData, Table, String, Column, Integer, Text, DateTime, Boolean
import fastapi
import csv
import random


api = fastapi.FastAPI()
@api.get('/')
async def hello():
    return {'hello': 'World'}


def read_products():
    with open('products.csv', 'r', newline='') as csvfile:
        table_names = csvfile.readline()
        table_names = table_names[:len(table_names)-2]
        file_reader = csv.reader(csvfile, delimiter=',')
        product_list = list()
        for line in file_reader:
            product_list.append(line)
        return table_names, product_list


tables, products = read_products()
metadata = MetaData()
print(tables)
print(products)


# table = Table('Доступные товары', metadata,
#               Column(tables[0], Integer(), primary_key=True),
#               Column(tables[1], Text(), nullable=False),
#               Column(tables[2], Integer(), nullable=False)
#               )
