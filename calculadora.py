def adicionar(x, y):
 return x+y
def subtrair(x,y):
 return x-y
def multiplicar(x,y):
 return x*y
def dividir(x,y):
 if y!=0:
  return x/y
 else:
  return('Erro:essa divisao ai nao funciona meu parca')
print('Escolha a operacao')
print("1 adicao")
print('2 subtracao')
print('3 multiplicacao')
print('4 divisao')

#pede pro usuario escolher uma operação

operacao=input('Digite o numero da operacao desejada (1/2/3/4)')

#pede pro usuario inserir dois numeros

num1=float(input('Digite o primeiro numero: '))
num2=float(input('Digite o segundo numero: '))

#Realiza operação escolhida
if operacao=='1':
 print('resultado: '.adicionar(num1,num2))
elif operacao==2:
 print('resultado: '.subtrair(num1,num2) )
elif operacao==3:
 print('resultado: '.multiplicar(num1,num2))
elif operacao==4:
 print('resultado: '.dividir(num1,num2))
else:
 print('nao foi possivel encontrar um resultado')







#tentativa1
def adicionar(x,y):
 return x+y
def subtrair(x,y):
 return x-y
def multiplicar(x,y):
 return x*y
def dividir(x,y):
 if y!=0:
  return x/y
 else:
  print('erro de operacao')

print('Escolha a operacao ')
print(' 1 Adicao')
print(' 2 subtracao')
print(' 1 multiplicacao')
print(' 1 divisao')


operacao=input('Digite o numero da operacao desejada')

num1=float(input('Digite o primeiro numero: '))
num2=float(input('Digite o segundo numero:'))

if operacao==1:
 print('resultado: '.adicao(num1,num2))
if operacao==2:
 print('resultado: '.subtracao(num1,num2))
if operacao==3:
 print('resultado: '.multiplicacao(num1,num2))
if operacao==4:
 print('resultado:'.divisao(num1,num2))






