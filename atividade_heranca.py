def lin():
    print("=" * 40)
#Exercício 1 – Identificando a herança Observe o código.

class Animal:
    def falar(self):
        print("O animal faz um som")

class Cachorro(Animal):
    def falar(self):
        print(f"O cachorro faz auau")
pass

dog = Cachorro()

dog.falar()
#Perguntas:
#1. Qual é a classe pai?
#Animal
#2. Qual é a classe filha?
#Cachorro
#3. Por que o cachorro consegue usar o método falar()?
#Pois ele coloca a classe pai em parenteses chamando os métodos da classe pai

#Exercício 2 – Criando outra classe filha
#Crie uma classe chamada Gato que herda da classe Animal.
class Animal:
    def falar(self):
        print("O animal faz um som")

class Gato(Animal):
    def falar(self):
        print(f"O gato faz miau")
pass
g = Gato()
g.falar()
#Pergunta:
#O método falar() foi criado na classe Gato ou herdado?
#Foi herdado

#Exercício 3 – Herdando atributos
#Complete o código para que o aluno possa acessar o atributo nome.
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
class Aluno(Pessoa):
     def nome(self):
        return(f"O nome do aluno é {self.nome}")
pass

a = Aluno()
print(a.nome)
#Perguntas:
#1. Onde o atributo nome foi criado?
#Na classe Pessoa
#2. Por que a classe Aluno consegue usar esse atributo?
#Ele coloca a classe mãe em paratenses para chamar os atributos

#Exercício 4 – Mudando o comportamento
#Complete o método da classe filha.

class Animal:
     def __init__(self, nome):
            self.nome = nome

     def falar(self):
       print(f"O animal faz um som")

class Cachorro(Animal):

    def falar(self):
        print(f" {self.nome} faz auau")
    

dog = Cachorro("Thor")
animal1 = ()
dog.falar()

#Faça o cachorro falar "O cachorro late".



#Exercício 5 – Criando um sistema simples
#Crie uma classe filha chamada Moto que herda da classe Veiculo.
class Veiculo:
    def mover(self):
     print("O veículo está se movendo")
class Moto(Veiculo):
    def mover(self):
       print("A moto está se movendo")
pass
m = Moto()
m.mover()
#A classe Moto criou o método mover() ou herdou?
#Ela herdeu

#Exercício 6 – Criando novos métodos
#Crie uma classe pai chamada Pessoa.
#Depois crie duas classes filhas:
#Aluno
#Professor
#Aluno deve ter método estudar()
#Professor deve ter método ensinar()
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
    
class Alunos(Pessoa):
    def estudar(self):
        return(f"{self.nome}, esta estudando")
    
class Professor(Pessoa):
    def ensinar(self):
        return(f"{self.nome}, está ensinando")
    
a = Alunos("Maria", 17)
p = Professor("Lucas", 22)


print(a.estudar())
print(p.ensinar())

#Exercício 7 – Sistema de animais
#Crie uma classe pai chamada Animal com atributo nome.
#Depois crie duas classes filhas:
#Cachorro
#Gato
#Cada classe deve ter seu próprio método falar().
class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def falar(self):
        print(f"O {self.nome} faz au,au!")

class Gato(Animal):
    def falar(self):
        print(f"O {self.nome} faz miau, miau!")

c1 = Cachorro("Bob")
g1 = Gato("Anakin")
c1.falar()
g1.falar()


#Exercício 8 – Usando construtor com herança
#Complete o código usando herança.
#Crie um objeto Professor e chame o método ensinar()
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Professor(Pessoa):

    def ensinar(self):
        print(self.nome, "está ensinando")

professor = Professor("João")
professor.ensinar()

#Exercício 9 – Sistema de veículos
#Crie uma classe pai chamada Veiculo com:
#atributo marca
#método mover()
#Depois crie duas classes filhas:
#Carro
#Moto
#Cada uma deve imprimir uma mensagem diferente ao se mover.

class Veiculos:
    def __init__(self, marca):
        self.marca = marca

    def mover(self):
        (f"O veículo da marca{self.marca} está se movendo")

class Carro(Veiculos):
    def mover(self):
        print(f"O carro da marca {self.marca} está se movimentando para frente!")

class Moto(Veiculos):
    def mover(self):
        print(f"A moto da marca{self.marca} está se movendo para trás")      

c1 = Carro("Toyta")
m1 = Moto("Honda") 

c1.mover()
m1.mover()

#Exercício 10 – Mini sistema de jogo
#Crie uma classe chamada Personagem com:
#atributo nome
#método atacar()
#Depois crie duas classes filhas:
#Guerreiro
#Mago
#Cada personagem deve atacar de forma diferente.
#Exemplo de saída esperada:
#Thor ataca com espada
#Merlin lança magia
#Classe pai → define características gerais
#Classe filha → herda essas características e pode modificá-las

class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print(f"O {self.nome} atacou o oponente")

class Guerreiro(Personagem):
    def atacar(self):
        print(f"{self.nome} ataca com espada")

class Mago(Personagem):
    def atacar(self):
        print(f"{self.nome} lança magia")

g1 = Guerreiro("Thanos")
m1 = Mago("Wanda")

g1.atacar()
m1.atacar()


