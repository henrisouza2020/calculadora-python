'''entrada = input('Digite um numero: ')

if entrada.isdigit():
    entrada_int= int(entrada)
    par_impar = entrada_int % 2 == 0 
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'
    print(f'o numero {entrada_int} é {par_impar_texto}')
else:
    print('Voce nao digitou um numero inteiro')





'''
'''entrada = input(' Digite a hora em numeros inteiros: ')

try:
    hora= int(entrada)

    if hora>=6 and hora<= 11:
        print('Bom dia ')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora<= 23:
        print('Boa noite')
    elif hora >=0 and hora <= 5:
        print('Boa madrugada')
    else:
        print('horario nao existe')
except:
    print('Por favor digite numeros inteiros')
'''

nome=input('Digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <=4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome<=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais uma letra')