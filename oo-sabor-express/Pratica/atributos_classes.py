print('\nMódulo 2: Métodos especiais e atributos\n')

print('\n1. Criando uma classe chamada Carro')
class   Carro():
    def __init__(self, nome, modelo, cor, ano):
        self.nome = nome
        self.modelo = modelo 
        self.cor = cor
        self.ano = ano

# Instanciando um carro e atribuindo valores aos seus atributos
carro1 = Carro('HB20', 'Confort Plus', 'Preto', 2018)
carro2 = Carro('Nivus', 'SUV', 'Prata', 2022)   
print(carro1)
print(carro2)

print('\n2. Criando uma classe chamada Restaurante')
class Restaurante():
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
# Instanciando um restaurante e atribuindo valores aos seus atributos  
restaurante1 = Restaurante('Divino fogão', 'Feijoada')
restaurante2 = Restaurante('Girrafas', 'Arroz e feijão')

print(restaurante1)
print(restaurante2)

print('\n3. Criando uma classe chamada Cliente')
class Cliente:

    clientes = []

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        Cliente.clientes.append(self)

    def listando_clientes():
        for cliente in Cliente.clientes:
            print(f'Nome:{cliente.nome} | Idade:{cliente.idade} | Email:{cliente.email}')

cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com')
cliente2 = Cliente(nome='Agatha', idade=30, email='agatha@gmail.com')
cliente3 = Cliente(nome='Julia', idade=35, email='julia@gmail.com')
cliente4 = Cliente(nome='Jonatha', idade=40, email='jonatha@gmail.com')
cliente5 = Cliente(nome='Carlos', idade=45, email='carlos@gmail.com')

Cliente.listando_clientes()