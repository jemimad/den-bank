from flask import Flask, request, Response

app = Flask(__name__)
bd = {}

@app.route('/cadastro', methods=['POST'])
def cadastrar_conta():
  numero_conta = request.json['numero']
  if numero_conta in bd:
    return 'Conta já cadastrada', 409
  else:
    bd[numero_conta] = 0
    return '', 201

@app.route('/saldo', methods=['GET'])
def consultar_saldo():
  numero_conta = int(request.args['numero'])

  if numero_conta in bd:
    return str(bd[numero_conta]), 200
  else:
    return 'Conta inexistente', 404

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
  app.run(debug=True)