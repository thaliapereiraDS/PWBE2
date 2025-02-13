from datetime import datetime

# Classe Fornecedor
class Fornecedor:
    def __init__(self, nome, tipo_servico):
        self.nome = nome
        self.tipo_servico = tipo_servico
    
    def __str__(self):
        return f"{self.nome} ({self.tipo_servico})"

# Classe Evento
class Evento:
    def __init__(self, nome, data, local, descricao):
        self.nome = nome
        self.data = data
        self.local = local
        self.descricao = descricao
        self.tarefas = []
        self.fornecedores = []

    def adicionar_tarefa(self, nome, prazo, responsavel):
        self.tarefas.append(f"Tarefa: {nome} - Prazo: {prazo} - Responsável: {responsavel}")

    def adicionar_fornecedor(self, nome, tipo_servico):
        self.fornecedores.append(Fornecedor(nome, tipo_servico))
    
    def __str__(self):
        return f"{self.nome} - {self.data} - {self.local} - {self.descricao}"

# Função para capturar dados do usuário
def criar_evento():
    nome = input("Nome do evento: ")
    data = datetime.strptime(input("Data do evento (dd/mm/aaaa): "), "%d/%m/%Y")
    local = input("Local do evento: ")
    descricao = input("Descrição do evento: ")
    
    evento = Evento(nome, data, local, descricao)
    
    while True:
        tarefa_nome = input("Nome da tarefa (ou 'fim' para parar): ")
        if tarefa_nome.lower() == 'fim':
            break
        prazo = input("Prazo da tarefa (dd/mm/aaaa): ")
        responsavel = input("Responsável pela tarefa: ")
        evento.adicionar_tarefa(tarefa_nome, prazo, responsavel)
    
    while True:
        fornecedor_nome = input("Nome do fornecedor (ou 'fim' para parar): ")
        if fornecedor_nome.lower() == 'fim':
            break
        tipo_servico = input("Tipo de serviço: ")
        evento.adicionar_fornecedor(fornecedor_nome, tipo_servico)
    
    return evento

# Exemplo de uso:
evento = criar_evento()
print(f"\nEvento Criado: {evento}")
print("\nTarefas:")
for tarefa in evento.tarefas:
    print(tarefa)
print("\nFornecedores:")
for fornecedor in evento.fornecedores:
    print(fornecedor)
