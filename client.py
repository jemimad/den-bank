import requests
base_url = 'http://127.0.0.1:5000/'

def listar_operacoes():
  print()
  print('==========================================================================')
  print('                            MENU DE OPERAÇÕES                            ')
  print('==========================================================================')
  print()
  print('1 - Cadastrar nova conta             2 - Consultar saldo                  ')
  print('3 - Depositar valor                  4 - Sacar valor')
  print('5 - Transferir valor                 6 - Listar operações')
  print('7 - Sair')


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

def sacar_valor():
  print()
  print('==========================================================================')
  numero = int(input('Informe o número da conta: '))
  print('--------------------------------------------------------------------------')
  valor = float(input('Informe o valor a ser sacado: '))
  print('--------------------------------------------------------------------------')
  response = requests.post(base_url + '/saque', json={'numero': numero, 'valor':valor})
  print(response.text)
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
    pass
  elif operacao == '2':
    apresentar_saldo()
  elif operacao == '3':
    pass
  elif operacao == '4':
    sacar_valor()
  elif operacao == '5':
    pass
  elif operacao == '6':
    listar_operacoes()    
  elif operacao == '7':
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