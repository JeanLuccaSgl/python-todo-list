def adicionarTarefa(listaTarefas):
    geradorId = 0
    idUsuario = 0

    for tarefa in listaTarefas:       #Loop for pra veriicar qual o maior id, independente da ordem
        if tarefa["id"] > geradorId:
            geradorId = tarefa["id"]

    geradorId += 1

    nomeTarefa = input("Digite o nome da sua tarefa: ")

    statusTarefa = False

    infoDict = {
        "id": geradorId,
        "nome": nomeTarefa,
        "status": statusTarefa,
    }

    listaTarefas.append(infoDict)
    print("Tarefa adicionada com sucesso!")


def listarTarefa(listaTarefas):
    if not listaTarefas: #verificação se a lista tá vazia, retorna True se tiver, logo, não precisa ter o == True
        print("Nenhuma tarefa encontrada")

    for tarefa in listaTarefas:
        if tarefa["status"]:
           print(f'[X] {tarefa["id"]} - {tarefa["nome"]}')
        else:
            print(f'[ ] {tarefa["id"]} - {tarefa["nome"]}')


def concluirTarefa(listaTarefas):
    encontrou = False

    idUsuario = int(input("Digite o ID da tarefa que você quer mudar o status: "))

    for tarefa in listaTarefas:
        if tarefa["id"] == idUsuario:
            encontrou = True
            if tarefa["status"]:
                print("A tarefa já foi concluída!")
                break
            else:
                tarefa["status"] = True
                print("Tarefa marcada como concluída com sucesso!")

            break

    if not encontrou:
        print("Não existe nenhuma tarefa com esse ID.")


def removerTarefa(listaTarefas):
    encontrou = False

    idUsuario = int(input("Digite o ID da tarefa que você quer excluir a tarefa: "))

    for tarefa in listaTarefas:
        if tarefa["id"] == idUsuario:
            encontrou = True
            listaTarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
            break

    if not encontrou:
        print("Não existe nenhuma tarefa com esse ID.")



