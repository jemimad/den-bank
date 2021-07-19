from flask import Flask, request, Response

app = Flask(__name__)
bd = {}

@app.route('/cadastro', methods=['POST'])
def cadastrar_conta():
  return '', 501

@app.route('/saldo', methods=['GET'])
def consultar_saldo():
  return '', 501

@app.route('/deposito', methods=['POST'])
def depositar_valor():
  return '', 501

@app.route('/saque', methods=['POST'])
def sacar_valor():
  return '', 501

@app.route('/transferencia', methods=['POST'])
def transferir_valor():
  return '', 501

if __name__ == '__main__':
  app.run()