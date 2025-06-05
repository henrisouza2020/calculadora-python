while True:
    numero_1 = input('Digite um numero:  ')
    numero_2 = input('Digite um numero:  ')
    operador = input('Digite um operador:  ')

    numero_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None

    if numero_validos is None:
        print('Um ou ambos os numeros digitados sao invalidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta. Confira o resultado logo abaixo:')

    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Nao era pra ter chegado aqui')

    sair = input('Quer sair? [s]im:  ').lower().startswith('s')
    if sair:
        break