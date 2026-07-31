import json
from json import JSONDecodeError


def carregarTarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            dados = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
            return []
    return dados

def salvarTarefas(listaTarefas):
    with open("tarefas.json", "w") as arquivo: #"tarefas.json" onde o arquivo vai salvar | "w" write, se o arquivo não existir ele cria, se existir ele escreve por cima do existente
        dados = json.dump(listaTarefas, arquivo, indent=4) #dump recebe o objeto que quero salvar (listaTareffas), o arquivo aberto (tarefas.json) e o indent pra deixar bonito