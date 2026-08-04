def adicionarTarefa(listaTarefas):
    geradorId = 0
    idUsuario = 0

    for tarefa in listaTarefas:       #Loop for pra veriicar qual o maior id, independente da ordem
        if tarefa["id"] > geradorId:
            geradorId = tarefa["id"]

    geradorId += 1

    while True:                                                       #Verificação se o campo nomeTarefa está preenchido
        nomeTarefa = input("Digite o nome da sua tarefa: ").strip().lower()

        if nomeTarefa:
            break

        print("O nome da tarefa não pode estar vazio.")

    for tarefa in listaTarefas:
        if nomeTarefa == tarefa["nome"].lower():
            while True:
                opcAddNovamente = input("Já existe uma tarefa com esse nome. Deseja adicioná-la novamente? (S/N): ").upper()

                if opcAddNovamente in ("S", "SIM"):
                    break

                elif opcAddNovamente in ("N", "NAO", "NÃO"):
                    return

                else:
                    print("Digite um valor válido.")



    statusTarefa = False             #Define o status como falso/não concluído automaticamente

    infoDict = {                     #Criação do dicionário
        "id": geradorId,
        "nome": nomeTarefa,
        "status": statusTarefa,
    }

    listaTarefas.append(infoDict)             #Inclui o novo dicionário/tarefa na lista
    print("Tarefa adicionada com sucesso!")


def listarTarefa(listaTarefas):
    if not listaTarefas: #Verificação se a lista tá vazia, retorna True se tiver, logo, não precisa ter o == True
        print("Nenhuma tarefa encontrada")
        return

    for tarefa in listaTarefas: #Percorre a lista de tarefas e se alguma estiver com status True/Concluído ele marca com [X], senão com [ ]
        if tarefa["status"]:
           print(f'[X] {tarefa["id"]} - {tarefa["nome"]}')
        else:
            print(f'[ ] {tarefa["id"]} - {tarefa["nome"]}')

def pesquisarNome(listaTarefas):
    encontrou = False

    if not listaTarefas: #Verificação se a lista tá vazia
        print("Nenhuma tarefa encontrada")
        return

    nomeTarefaUser = input("Digite o nome da sua tarefa: ").strip().lower()

    if not nomeTarefaUser:
        print("Por favor, digite um nome válido.")
        return

    for tarefa in listaTarefas:
        if nomeTarefaUser in tarefa["nome"].lower():
            encontrou = True

            if tarefa["status"]:
                print(f'[X] {tarefa["id"]} - {tarefa["nome"]}')

            else:
                print(f'[ ] {tarefa["id"]} - {tarefa["nome"]}')

    if not encontrou:
        print("Nenhuma tarefa encontrada")

def concluirTarefa(listaTarefas):
    encontrou = False        #Variável para verificação se o id realmente existe, inicialmente não encontrou

    if not listaTarefas: #Verificação se a lista tá vazia, retorna True se tiver, logo, não precisa ter o == True
        print("Nenhuma tarefa encontrada")
        return

    listarTarefa(listaTarefas)

    while True:              #Loop e verificação de valor do usuário, se preencher sem um número, mostra mensagem e pede pra digitar novamente
        try:
            idUsuario = int(input("Digite o ID da tarefa que você quer mudar o status: "))
            break

        except ValueError:
            print("O campo deve ser preenchido corretamente.")

    for tarefa in listaTarefas:             #Loop pra verificar o id da tarefa digitada pelo usuário, se encontrar altera o status de "encontrou" pra True
        if tarefa["id"] == idUsuario:
            encontrou = True

            if tarefa["status"]:                          #Verificação se a tarefa já foi concluída ou não, se não foi altera o status e mostra mensagem
                print("A tarefa já foi concluída!")
                break

            else:
                tarefa["status"] = True
                print("Tarefa marcada como concluída com sucesso!")

            break

    if not encontrou:                                           #Se não existe nenhuma tarefa com aquele id o sistema informa
        print("Não existe nenhuma tarefa com esse ID.")


def removerTarefa(listaTarefas):                                #Lógica semelhante a função de concluir tarefa, mas removendo
    encontrou = False

    if not listaTarefas: #Verificação se a lista tá vazia, retorna True se tiver, logo, não precisa ter o == True
        print("Nenhuma tarefa encontrada")
        return

    listarTarefa(listaTarefas)

    while True:
        try:
            idUsuario = int(input("Digite o ID da tarefa que você quer excluir: "))
            break
        except ValueError:
            print("O campo deve ser preenchido corretamente.")

    for tarefa in listaTarefas:
        if tarefa["id"] == idUsuario:
            encontrou = True

            listaTarefas.remove(tarefa)

            print("Tarefa removida com sucesso!")
            break

    if not encontrou:
        print("Não existe nenhuma tarefa com esse ID.")

def estatisticas(listaTarefas):
    if not listaTarefas: #Verificação se a lista tá vazia, retorna True se tiver, logo, não precisa ter o == True
        print("Nenhuma tarefa encontrada")
        return

    tarefasTotal = len(listaTarefas)

    tarefasPendentes = 0
    tarefasConcluidas = 0

    for tarefa in listaTarefas:
        if tarefa["status"]:
            tarefasConcluidas += 1
        else:
            tarefasPendentes += 1

    percentualConcluidas = (tarefasConcluidas / tarefasTotal) * 100
    percentualPendentes = (tarefasPendentes / tarefasTotal) * 100

    print("ESTATÍSTICAS")
    print("-----------------")

    print(f"Total de Tarefas: {tarefasTotal}")
    print()

    print(f"Concluídas: {tarefasConcluidas}")
    print(f"Pendentes: {tarefasPendentes}")
    print()

    print(f"% Concluídas: {percentualConcluidas:.2f}%")
    print(f"% Pendentes: {percentualPendentes:.2f}%")
