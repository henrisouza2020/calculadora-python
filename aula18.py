#operadores lógicos
#and (e) or (ou) not(não)
#and - todas as condições precisam ser verdadeiras
#Se qualquer valor for considerado falso,a expressão inteira será avaliada naquele valor
#Também existe o tipo none que é considerado um não valor

entrada=input('[E]ntrar [s]air:' )
senha_digitada= input('Senha:' )

senha_permitida='123456'
#if True

if entrada== 'E' and senha_digitada== senha_permitida:
    print('Voce entrou no sistema')
else:
    print('Senha incorreta')


if 1 and 1:
    print(True and 1 and False)
