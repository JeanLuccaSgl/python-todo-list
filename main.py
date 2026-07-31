import tarefas
from storage import carregarTarefas, salvarTarefas


def mostrarMenu():
    print(
        "------------------\n"
        "Menu de Opções\n"
        "1. Adicionar\n"
        "2. Listar Tarefas\n"
        "3. Concluir\n"
        "4. Remover\n"
        "5. Sair\n"
    )
listaTarefas = carregarTarefas()
opcUser = 0

while True:
    mostrarMenu()
    try:
        opcUser = int(input("Digite uma opção válida: "))
    except ValueError:
        print("Valor inválido, digite novamente")
        continue

    if opcUser == 1:
        tarefas.adicionarTarefa(listaTarefas)

    elif opcUser == 2:
        tarefas.listarTarefa(listaTarefas)

    elif opcUser == 3:
        tarefas.concluirTarefa(listaTarefas)

    elif opcUser == 4:
        tarefas.removerTarefa(listaTarefas)

    elif opcUser == 5:
        salvarTarefas(listaTarefas)
        break