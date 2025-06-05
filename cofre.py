def menu():
 print('o que deseja fazer?')
 print('1 - Adicionar dinheiro')
 print('2 - Remover dinheiro')
 print('3 - Exibir o total acumulado')
 escolha=input('Digite o numero:')
 return escolha
cofre=[]
while True:
 escolha= menu()
 if escolha=='1':
  quantia= float(input('Quanto de dinheiro deseja adicionar ao cofre?'))
  cofre.append(quantia)
  print(f'{quantia}foi adicionada ao cofre')
 elif escolha=='2':
  quantia= float(input('Quanto voce deseja remover do cofre?'))
  if sum(cofre) >=quantia:
   cofre.remove(quantia)
   print(f'{quantia} foi removida do cofre')
 elif escolha=='3':
  total_acumulado=sum(cofre)
  print(f'Total acumulado no cofre:{total_acumulado}')
 elif escolha=='4':
  print('Saindo do programa')
  break
 else:
  print('Opção invalida')
 
 
 