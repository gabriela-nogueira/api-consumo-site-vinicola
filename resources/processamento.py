from flask_restful import Resource, reqparse
import csv
import requests
from io import StringIO

def get_dict_processamento():

    tipos_processamento = ['Viniferas','Americanas','Mesa','Semclass']
    csv_data = []

    for processamento in tipos_processamento:
        csv_data.append({'id_processamento': tipos_processamento.index(processamento), 'tipo_processamento' : processamento})
        url = f"http://vitibrasil.cnpuv.embrapa.br/download/Processa{processamento}.csv"
        response = requests.get(url)

        with StringIO(response.text) as csv_file:
            reader = csv.DictReader(csv_file, delimiter='\t')
            for row in reader:
                csv_data[tipos_processamento.index(processamento)]['dados'] = dict(row)

    return csv_data

class Processamento(Resource):

    def get(self):
        dados = get_dict_processamento()
        return dados