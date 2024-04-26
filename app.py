from flask import Flask
from flask_restful import Api
from resources.producao import Producao, Ano, Produto
from resources.processamento import Processamento

app = Flask(__name__)
api = Api(app)

api.add_resource(Producao, '/producao')
api.add_resource(Ano, '/producao/ano/<string:ano>')
api.add_resource(Produto, '/producao/produto/<string:id>')
api.add_resource(Processamento, '/processamento')

if __name__ == '__main__':
    app.run(debug=True)