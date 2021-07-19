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
    pass
  elif operacao == '3':
    pass
  elif operacao == '4':
    pass
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