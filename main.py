import tarefas
from storage import carregarTarefas, salvarTarefas


def mostrarMenu():
    print(
        "------------------\n"
        "Menu de Opções\n"
        "1. Adicionar\n"
        "2. Listar Tarefas\n"
        "3. Pesquisar Tarefa\n"
        "4. Concluir\n"
        "5. Remover\n"
        "6. Estatísticas\n"
        "7. Sair\n"
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
        tarefas.pesquisarNome(listaTarefas)

    elif opcUser == 4:
        tarefas.concluirTarefa(listaTarefas)

    elif opcUser == 5:
        tarefas.removerTarefa(listaTarefas)

    elif opcUser == 6:
        tarefas.estatisticas(listaTarefas)

    elif opcUser == 7:
        salvarTarefas(listaTarefas)
        break