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
    return 'Conta cadastrada com sucesso!', 201

@app.route('/saldo', methods=['GET'])
def consultar_saldo():
  numero_conta = int(request.args['numero'])

  if numero_conta in bd:
    return str(bd[numero_conta]), 200
  else:
    return 'Conta inexistente', 404

@app.route('/deposito', methods=['POST'])
def depositar_valor():
  numero_conta = request.json['numero']
  
  if numero_conta in bd:
    valor = request.json['valor']
    
    bd[numero_conta] += valor
    return 'Depósito efetuado com sucesso!', 200
  else:
    return 'Conta inexistente', 404

@app.route('/saque', methods=['POST'])
def sacar_valor():
  numero_conta = request.json['numero']
  
  if numero_conta in bd:
    valor = request.json['valor']
    
    bd[numero_conta] -= valor
    return 'Saque efetuado com sucesso!', 200
  else:
    return 'Conta inexistente', 404

@app.route('/transferencia', methods=['POST'])
def transferir_valor():
  numero_conta_origem = request.json['numeroOrigem']
  numero_conta_destino = request.json['numeroDestino']

  if numero_conta_origem in bd:

    if numero_conta_destino in bd:
      valor = request.json['valor']

      bd[numero_conta_origem] -= valor
      bd[numero_conta_destino] += valor

      return 'Tranferência efetuada com sucesso!', 200
    else:
      return 'Conta de destino inexistente', 404

  else:
    return 'Conta de origem inexistente', 404
    
if __name__ == '__main__':
  app.run(debug=True)