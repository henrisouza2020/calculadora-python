def menu():
    print('Escolha uma opção')
    print('1 - Adicionar uma nova Tarefa')
    print('2 - Exibir lista de tarefas')
    print('3 - Marcar uma tarefa como concluida')
    print('4 - Remover Tarefa')
    print('5 - Sair do programa')

escolha=input('Digite o numero da opção:')   
escolha

tarefas=[]
while True:
    escolha=menu()
    if escolha=='1':
     nova_tarefa=input('Digite sua nova tarefa:')
     tarefas.append(nova_tarefa)
     print('tarefa adicionada com sucesso')
    if escolha=='2':
      print('Lista de tarefas:')
    for i,tarefa in enumerate(tarefas, start=1):
      print(f'{i}. {tarefa}')
    if escolha=='3':
       print('Lista de tarefas:')
    for i, tarefa in enumerate(tarefas,start='1'):
       print(f'{i}. {tarefas}')
       indice= int(input('Digite o numero da tarefa que voce concluiu:')) -1
    if 0<=indice <len(tarefas):
       tarefas[indice]+= '- Concluida'
       print('tarefa marcada como concluida')
    else:
        print('Numero invalido')
    if escolha== '4':
        # Remover uma tarefa
        print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
         print(f"{i}. {tarefa}")
         indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
    if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida com sucesso.")
    else:
            print("Número inválido.")
    if escolha == '5':
        # Sair do programa
        print("Saindo do programa.")
        break
    
    else:
     print("Opção inválida. Tente novamente.")       

