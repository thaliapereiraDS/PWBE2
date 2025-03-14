#1-classe circulo
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.raio


circulo = Circulo(5)
print(f'Área: {circulo.area()}')
print(f'Perímetro: {circulo.perimetro()}')

 
#2-  Classe ContaBancária

class ContaBancária:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")


conta = ContaBancária(12345, "João", 1000)
conta.deposito(500)
conta.saque(200)
print(f'Saldo atual: {conta.saldo}')


#3. Classe Retângulo

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


retangulo = Retangulo(4, 6)
print(f'Área: {retangulo.area()}')
print(f'Perímetro: {retangulo.perimetro()}')


#4. Classe Aluno
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def situacao(self):
        return "Aprovado" if self.media() >= 7 else "Reprovado"

aluno = Aluno("Maria", "123")
aluno.adicionar_nota(8)
aluno.adicionar_nota(6)
print(f'Média: {aluno.media()}')
print(f'Situação: {aluno.situacao()}')


#5. Classe Funcionário

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def salario_liquido(self):
        impostos = 0.2 * self.salario  # Exemplo: 20% de impostos
        beneficios = 0.1 * self.salario  # Exemplo: 10% de benefícios
        return self.salario - impostos + beneficios


funcionario = Funcionario("Carlos", 5000, "Analista")
print(f'Salário líquido: {funcionario.salario_liquido()}')

#6- Classe Produto

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

    def esta_disponivel(self):
        return self.quantidade > 0

produto = Produto("Camiseta", 50, 10)
print(f'Valor total em estoque: {produto.valor_total()}')
print(f'Disponível: {produto.esta_disponivel()}')


#7- Classe Triângulo
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def e_valido(self):
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)

    def area(self):
        if not self.e_valido():
            return "Triângulo inválido"
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        return area

triangulo = Triangulo(3, 4, 5)
print(f'É válido? {triangulo.e_valido()}')
print(f'Área: {triangulo.area()}')



#8. Classe Carro
class Carro:
    def __init__(self, marca, modelo, velocidade_atual=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual

    def acelerar(self, incremento):
        self.velocidade_atual += incremento

    def frear(self):
        self.velocidade_atual = 0

carro = Carro("Fusca", "1969")
carro.acelerar(60)
print(f'Velocidade atual: {carro.velocidade_atual}')
carro.frear()
print(f'Velocidade após frear: {carro.velocidade_atual}')


#9. Classe Paciente

class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.consultas = []

    def adicionar_consulta(self, data):
        self.consultas.append(data)

    def exibir_consultas(self):
        return self.consultas

paciente = Paciente("Ana", 30)
paciente.adicionar_consulta("12/02/2025")
print(f'Consultas: {paciente.exibir_consultas()}')


#10. Classe Livro

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f'Livro {self.titulo} emprestado.'
        return f'Livro {self.titulo} não disponível.'

    def devolver(self):
        self.disponivel = True

livro = Livro("Python para Iniciantes", "João Silva", 200)
print(livro.emprestar())
livro.devolver()
print(livro.emprestar())





#11. Classe Banco

class Banco:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def abrir_conta(self, numero, titular):
        conta = ContaBancária(numero, titular)
        print(f'Conta aberta para {titular}')
        return conta

banco = Banco()
conta = banco.abrir_conta(123, "Maria")
conta.deposito(1000)
print(f'Saldo da conta: {conta.saldo}')





#12. Classe LojaVirtual

class LojaVirtual:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total_compra(self):
        return sum([produto.preco * produto.quantidade for produto in self.produtos])

loja = LojaVirtual()
produto1 = Produto("Celular", 1000, 2)
produto2 = Produto("Notebook", 3000, 1)
loja.cadastrar_produto(produto1)
loja.cadastrar_produto(produto2)
print(f'Total da compra: {loja.calcular_total_compra()}')


#13. Classe Agenda

class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        self.contatos[nome] = telefone

    def editar_contato(self, nome, novo_telefone):
        self.contatos[nome] = novo_telefone

    def remover_contato(self, nome):
        del self.contatos[nome]

    def buscar_contato(self, nome):
        return self.contatos.get(nome, "Contato não encontrado")

agenda = Agenda()
agenda.adicionar_contato("Carlos", "123456789")
print(agenda.buscar_contato("Carlos"))
agenda.editar_contato("Carlos", "987654321")
print(agenda.buscar_contato("Carlos"))




#14. Classe MáquinaDeVendas

class MaquinaDeVendas:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, nome, preco, quantidade):
        self.produtos[nome] = {"preco": preco, "quantidade": quantidade}

    def selecionar_produto(self, nome):
        if nome in self.produtos and self.produtos[nome]["quantidade"] > 0:
            return self.produtos[nome]["preco"]
        return "Produto indisponível"

    def inserir_dinheiro(self, valor, nome_produto):
        preco = self.selecionar_produto(nome_produto)
        if isinstance(preco, float) and valor >= preco:
            self.produtos[nome_produto]["quantidade"] -= 1
            return valor - preco
        return "Dinheiro insuficiente ou produto indisponível"

maquina = MaquinaDeVendas()
maquina.cadastrar_produto("Refrigerante", 3.50, 10)
print(maquina.selecionar_produto("Refrigerante"))
troco = maquina.inserir_dinheiro(5, "Refrigerante")
print(f'Troco: {troco}')




#15. Classe JogoCartas

import random

class JogoCartas:
    def __init__(self):
        self.cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.baralhado = False

    def embaralhar(self):
        random.shuffle(self.cartas)
        self.baralhado = True

    def distribuir_cartas(self, jogadores):
        if not self.baralhado:
            self.embaralhar()
        distribuidas = {jogador: self.cartas.pop() for jogador in jogadores}
        return distribuidas
    
jogo = JogoCartas()
jogo.embaralhar()
jogadores = ['Jogador 1', 'Jogador 2']
cartas = jogo.distribuir_cartas(jogadores)
print(cartas)



import random
import calendar
from datetime import datetime

# 16. Classe RedeSocial
class RedeSocial:
    def __init__(self):
        self.usuarios = {}
        self.posts = []
    
    def adicionar_amigo(self, usuario, amigo):
        if usuario not in self.usuarios:
            self.usuarios[usuario] = {"amigos": [], "posts": []}
        if amigo not in self.usuarios:
            self.usuarios[amigo] = {"amigos": [], "posts": []}
        self.usuarios[usuario]["amigos"].append(amigo)
        self.usuarios[amigo]["amigos"].append(usuario)
    
    def publicar_mensagem(self, usuario, mensagem):
        if usuario not in self.usuarios:
            self.usuarios[usuario] = {"amigos": [], "posts": []}
        self.usuarios[usuario]["posts"].append(mensagem)
        self.posts.append({"usuario": usuario, "mensagem": mensagem})
    
    def comentar_post(self, usuario, post_index, comentario):
        if post_index < len(self.posts):
            post = self.posts[post_index]
            if "comentarios" not in post:
                post["comentarios"] = []
            post["comentarios"].append({"usuario": usuario, "comentario": comentario})
    
    def buscar_usuario(self, nome_usuario):
        return nome_usuario in self.usuarios

rede_social = RedeSocial()
rede_social.adicionar_amigo("Alice", "Bob")
rede_social.publicar_mensagem("Alice", "Oi, pessoal!")
rede_social.comentar_post("Bob", 0, "Oi, Alice!")
print("Usuário Alice existe?", rede_social.buscar_usuario("Alice"))  # True


# 17. Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.emprestimos = {}
    
    def cadastrar_livro(self, livro, autor):
        self.livros[livro] = {"autor": autor, "disponivel": True}
    
    def emprestar_livro(self, livro, usuario):
        if livro in self.livros and self.livros[livro]["disponivel"]:
            self.livros[livro]["disponivel"] = False
            self.emprestimos[livro] = usuario
        else:
            print("Livro não disponível.")
    
    def devolver_livro(self, livro):
        if livro in self.emprestimos:
            self.livros[livro]["disponivel"] = True
            del self.emprestimos[livro]
    
    def verificar_disponibilidade(self, livro):
        return self.livros.get(livro, {}).get("disponivel", False)
    
biblioteca = Biblioteca()
biblioteca.cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien")
biblioteca.emprestar_livro("O Senhor dos Anéis", "Carlos")
print("Livro disponível?", biblioteca.verificar_disponibilidade("O Senhor dos Anéis"))  # False
biblioteca.devolver_livro("O Senhor dos Anéis")
print("Livro disponível?", biblioteca.verificar_disponibilidade("O Senhor dos Anéis"))  # True


# 18. Classe Calendario
class Calendario:
    def exibir_mes(self, ano, mes):
        return calendar.month(ano, mes)
    
    def verificar_feriado(self, data):
        # Exemplo simples, você pode adicionar mais feriados
        feriados = ["01-01", "25-12"]
        return data.strftime("%d-%m") in feriados
    
    def diferenca_dias(self, data1, data2):
        return (data2 - data1).days

calendario = Calendario()
print("Calendário de Fevereiro de 2025:")
print(calendario.exibir_mes(2025, 2))  # Exibe o mês de fevereiro de 2025
data1 = datetime(2025, 2, 13)
data2 = datetime(2025, 3, 1)
print("Diferença de dias entre 13/02/2025 e 01/03/2025:", calendario.diferenca_dias(data1, data2))  # Diferença em dias


# 19. Classe JogoAdivinhacao
class JogoAdivinhacao:
    def __init__(self):
        self.numero = random.randint(1, 100)
    
    def fazer_palpite(self, palpite):
        if palpite == self.numero:
            return "Acertou!"
        elif palpite < self.numero:
            return "O número é maior."
        else:
            return "O número é menor."

jogo = JogoAdivinhacao()
palpite = 50
print(f"Palpite: {palpite} - Resultado: {jogo.fazer_palpite(palpite)}")  # Resposta se o palpite for maior ou menor


# 20. Jogo de Tabuleiro (Exemplo simplificado de Xadrez)
class Peca:
    def __init__(self, cor):
        self.cor = cor

class Rei(Peca):
    def movimentos_possiveis(self, posicao):
        # Exemplo simples de movimento
        return ["Cima", "Baixo", "Esquerda", "Direita", "Diagonal"]
    
class Torre(Peca):
    def movimentos_possiveis(self, posicao):
        return ["Vertical", "Horizontal"]

class Tabuleiro:
    def __init__(self):
        self.pecas = []
    
    def adicionar_peca(self, peca):
        self.pecas.append(peca)

tabuleiro = Tabuleiro()
rei = Rei("Branco")
torre = Torre("Preto")
tabuleiro.adicionar_peca(rei)
tabuleiro.adicionar_peca(torre)
print("Movimentos possíveis do Rei:", rei.movimentos_possiveis(None))  # Movimentos possíveis do Rei


# 21. Aplicação de E-commerce
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = []
    
    def adicionar_ao_carrinho(self, produto):
        self.carrinho.append(produto)
    
    def calcular_total(self):
        return sum([produto.preco for produto in self.carrinho])
    
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = cliente.carrinho
        self.total = cliente.calcular_total()

produto1 = Produto("Camiseta", 50)
cliente = Cliente("João")
cliente.adicionar_ao_carrinho(produto1)
pedido = Pedido(cliente)
print(f"Total do pedido de {cliente.nome}: R${pedido.total}")  # Total do pedido


# 22. Sistema de Estoque
class ProdutoEstoque:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def atualizar_quantidade(self, quantidade):
        self.quantidade += quantidade

class Compra:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        produto.atualizar_quantidade(quantidade)

class Venda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        produto.atualizar_quantidade(-quantidade)

produto = ProdutoEstoque("Notebook", 3000, 10)
compra = Compra(produto, 5)
venda = Venda(produto, 3)
print(f"Quantidade restante de {produto.nome}: {produto.quantidade}")  # Quantidade de produto após a compra e venda


# 23. Gerenciamento de Tarefas
class Tarefa:
    def __init__(self, nome, prioridade, data_vencimento, status):
        self.nome = nome
        self.prioridade = prioridade
        self.data_vencimento = data_vencimento
        self.status = status

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
    
    def listar_tarefas(self):
        return self.tarefas

tarefa1 = Tarefa("Estudar Python", "Alta", "2025-02-20", "Pendente")
gerenciador = GerenciadorTarefas()
gerenciador.adicionar_tarefa(tarefa1)
for t in gerenciador.listar_tarefas():
    print(f"Tarefa: {t.nome}, Status: {t.status}")


# 24. Sistema de Zoológico
class Animal:
    def __init__(self, nome, especie, dieta):
        self.nome = nome
        self.especie = especie
        self.dieta = dieta

class Zoologico:
    def __init__(self):
        self.animais = []
    
    def adicionar_animal(self, animal):
        self.animais.append(animal)

leao = Animal("Leão", "Felino", "Carnívoro")
zoologico = Zoologico()
zoologico.adicionar_animal(leao)
print("Animais no zoológico:", [animal.nome for animal in zoologico.animais])  # Nome dos animais no zoológico


# 25. Jogo de Combate
class Personagem:
    def __init__(self, nome, vida, forca, defesa):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.defesa = defesa
    
    def atacar(self, outro):
        dano = self.forca - outro.defesa
        outro.vida -= max(dano, 0)
    
    def esta_vivo(self):
        return self.vida > 0

guerreiro = Personagem("Guerreiro", 100, 20, 10)
mago = Personagem("Mago", 80, 30, 5)
guerreiro.atacar(mago)
print(f"Vida do Mago após ataque: {mago.vida}")  # Vida do mago após o ataque




