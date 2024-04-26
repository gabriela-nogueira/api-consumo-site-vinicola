from flask_restful import Resource, reqparse
import csv
import requests
from io import StringIO

def get_dict_producao():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    response = requests.get(url)

    csv_data = []

    with StringIO(response.text) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            csv_data.append(dict(row))

    return csv_data

class Producao(Resource):

    def get(self):
        dados = get_dict_producao()
        return dados


class Ano(Resource):

    def get(self, ano):
        dados = get_dict_producao()
        dados_por_ano = [{'id': row['id'] , 'produto': row['produto'], 'producao_do_ano': row[ano]} for row in dados]
        if dados_por_ano:
            return dados_por_ano, 200
        return {'message' : 'Ano não encontrado'}, 400

class Produto(Resource):

    def get(self, id):
        dados = get_dict_producao()
        dados_por_produto =  [row for row in dados if row['id'] == str(id)]
        if dados_por_produto:
            return dados_por_produto, 200
        return {'message' : 'Ano não encontrado'}, 400