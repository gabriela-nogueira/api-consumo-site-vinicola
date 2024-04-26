from flask_restful import Resource, reqparse
import csv
import requests
from io import StringIO

def get_dict_importacao():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    response = requests.get(url)

    csv_data = []

    with StringIO(response.text) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            csv_data.append(dict(row))

    return csv_data