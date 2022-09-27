import sqlalchemy
from sqlalchemy import MetaData, Table, String, Column, Integer, Text, DateTime, Boolean
import csv
import endpoints


def read_products():
    with open('products.csv', 'r', newline='') as csvfile:
        table_names = csvfile.readline()
        table_names = table_names[:len(table_names)-2]
        file_reader = csv.reader(csvfile, delimiter=',')
        product_list = list()
        for line in file_reader:
            product_list.append(line)
        return table_names, product_list


api = endpoints.api