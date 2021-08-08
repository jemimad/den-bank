import requests

base_url = 'http://127.0.0.1:5000'


def listar_operacoes():
    print()
    print('==========================================================================')
    print('                            MENU DE OPERAÇÕES                            ')
    print('==========================================================================')
    print()
    print('1 - Cadastrar nova conta             2 - Consultar saldo                  ')
    print('3 - Depositar valor                  4 - Sacar valor')
    print('5 - Transferir valor                 6 - Render juros')
    print('7 - Listar operações                 8 - Sair')


def cadastro_contas():
    print()
    print('==========================================================================')
    print()
    print('1 - Conta simples                    2 - Conta bônus                      ')
    print('3 - Conta poupança')

    print()
    print('==========================================================================')
    tipo = int(input('Informe o tipo da conta: '))
    numero = int(input('Informe o número da conta: '))
    saldo = 0
    if tipo == 3:
        saldo = float(input('Informe o saldo inicial:'))
    print('--------------------------------------------------------------------------')

    response = requests.post(base_url + '/cadastro',
                             json={'numero': numero, 'tipo': tipo, 'saldo':saldo})
    print(response.text)

    print('==========================================================================')


def transferir_valor():
    print()
    print('==========================================================================')
    numero_conta_origem = int(input('Informe o número da conta de origem: '))
    numero_conta_destino = int(input('Informe o número da conta de destino: '))
    valor = float(input('Informe o valor a ser transferido: '))
    print('--------------------------------------------------------------------------')

    response = requests.post(base_url + '/transferencia', json={
        'numeroOrigem': numero_conta_origem,
        'numeroDestino': numero_conta_destino,
        'valor': valor
    })
    print(response.text)

    print('==========================================================================')


def apresentar_saldo():
    print()
    print('==========================================================================')
    numero = input('Informe o número da conta: ')
    print('--------------------------------------------------------------------------')
    response = requests.get(base_url + '/saldo?numero=' + numero)

    if response.status_code == 200:
        print('O saldo é de', response.text, 'reais')
    else:
        print(response.text)
    print('==========================================================================')


def realizar_deposito():
    print()
    print('==========================================================================')
    numero = int(input('Informe o número da conta: '))
    valor = float(input('Informe o valor a ser depositado: '))
    print('--------------------------------------------------------------------------')

    response = requests.post(base_url + '/deposito',
                             json={'numero': numero, 'valor': valor})
    print(response.text)


def sacar_valor():
    print()
    print('==========================================================================')
    numero = int(input('Informe o número da conta: '))
    valor = float(input('Informe o valor a ser sacado: '))
    print('--------------------------------------------------------------------------')
    response = requests.post(
        base_url + '/saque', json={'numero': numero, 'valor': valor})
    print(response.text)
    print('==========================================================================')
    print('==========================================================================')

def render_juros():
    print()
    print('==========================================================================')
    numero = int(input('Informe o número da conta: '))
    valor = float(input('Informe a porcentagem de juros a ser aplicado no saldo: '))
    print('--------------------------------------------------------------------------')
    response = requests.post(base_url + '/render_juros', json={'numero': numero, 'valor':valor})
    print(response.text)
    print('==========================================================================')
    print('==========================================================================')

print('==========================================================================')
print(' _______   _______ .__   __.    .______        ___      .__   __.  __  ___ ')
print('|       \ |   ____||  \ |  |    |   _  \      /   \     |  \ |  | |  |/  / ')
print('|  .--.  ||  |__   |   \|  |    |  |_)  |    /  ^  \    |   \|  | |  \'  /  ')
print('|  |  |  ||   __|  |  . `  |    |   _  <    /  /_\  \   |  . `  | |    <   ')
print('|  \'--\'  ||  |____ |  |\   |    |  |_)  |  /  _____  \  |  |\   | |  .  \  ')
print('|_______/ |_______||__| \__|    |______/  /__/     \__\ |__| \__| |__|\__\ ')
print('                                                                           ')
print('                                                                    v1.0.0')
listar_operacoes()

while True:
    print()
    print('==========================================================================')
    operacao = input('Selecione uma operação: ')
    print('==========================================================================')

    if operacao == '1':
        cadastro_contas()
    elif operacao == '2':
        apresentar_saldo()
    elif operacao == '3':
        realizar_deposito()
    elif operacao == '4':
        sacar_valor()
    elif operacao == '5':
        transferir_valor()
    elif operacao == '6':
        render_juros()
    elif operacao == '7':
        listar_operacoes()
    elif operacao == '8':
        print()
        print('==========================================================================')
        print('Até mais!')
        print('==========================================================================')
        break
    else:
        print()
        print('==========================================================================')
        print('Operação inválida!')
        print('==========================================================================')
