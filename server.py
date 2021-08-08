from flask import Flask, request, Response

app = Flask(__name__)
bd = {}


@app.route('/cadastro', methods=['POST'])
def cadastrar_conta():
    numero_conta = request.json['numero']
    tipo_conta = request.json['tipo']

    if numero_conta in bd:
        return 'Conta já cadastrada', 409
    else:
        if tipo_conta == 1:  # Conta simples
            bd[numero_conta] = [1, 0]
            return 'Conta simples cadastrada com sucesso!', 201
        elif tipo_conta == 2:  # Conta Bônus
            bd[numero_conta] = [2, 0, 10]
            return 'Conta bônus cadastrada com sucesso!', 201
        elif tipo_conta == 3:  # Conta poupança
            bd[numero_conta] = [3, 0]
            return 'Conta poupança cadastrada com sucesso!', 201
        else:
            return 'Tipo de conta inexistente!', 400


@app.route('/saldo', methods=['GET'])
def consultar_saldo():
    numero_conta = int(request.args['numero'])

    if numero_conta in bd:
        return str(bd[numero_conta][1]), 200
    else:
        return 'Conta inexistente', 404


@app.route('/deposito', methods=['POST'])
def depositar_valor():
    numero_conta = request.json['numero']

    if numero_conta in bd:
        valor = request.json['valor']

        bd[numero_conta][1] += valor

        if bd[numero_conta][0] == 2:
            bd[numero_conta][2] += int(valor / 100)
            print(bd[numero_conta][2])

        return 'Depósito efetuado com sucesso!', 200
    else:
        return 'Conta inexistente', 404


@app.route('/saque', methods=['POST'])
def sacar_valor():
    numero_conta = request.json['numero']

    if numero_conta in bd:
        valor = request.json['valor']

        if (bd[numero_conta][0] == 1 or bd[numero_conta][0] == 2) and (bd[numero_conta][1] - valor < -1000): #Simples ou Bônus
            return 'Não há saldo suficiente para realizar o saque', 400
       
        bd[numero_conta][1] -= valor
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

            if (bd[numero_conta_origem][0] == 1 or bd[numero_conta_origem][0] == 2) and (bd[numero_conta_origem][1] - valor < -1000): #Simples ou Bônus
                return 'Não há saldo suficiente para realizar o saque', 400

            bd[numero_conta_origem][1] -= valor
            bd[numero_conta_destino][1] += valor

            if bd[numero_conta_destino][0] == 2:
                bd[numero_conta_destino][2] += int(valor / 150)
                print(bd[numero_conta_destino][2])
            return 'Tranferência efetuada com sucesso!', 200
        else:
            return 'Conta de destino inexistente', 404

    else:
        return 'Conta de origem inexistente', 404


@app.route('/render_juros', methods=['POST'])
def render_juros():
    numero_conta = request.json['numero']

    if numero_conta in bd:

        if bd[numero_conta][0] == 3:
            valor = request.json['valor']

            saldo_atual = bd[numero_conta][1]
            bd[numero_conta][1] += saldo_atual*(valor/100)

        else:
            return 'Conta não é poupança', 400

        return 'Juros aplicados com sucesso!', 200
    else:
        return 'Conta inexistente', 404


if __name__ == '__main__':
    app.run(debug=True)
