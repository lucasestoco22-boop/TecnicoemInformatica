class Animal: 
    def __init__(self, nome):
        self.nome = nome

        def som(self):
            return("O animal faz um som")

class Cachorro(Animal):
    def som(self):
        return(f"O {self.nome} faz au, au")
    
    def brincar(self):
        return(f"O {self.nome} quer brincar com Mimi")


class Gato(Animal):
    def som(self):
        return(f"O {self.nome} faz miau")
    
    def brincar(self):
        return(f"O {self.nome} sai correndo")

cachorro1 = Cachorro("Thor")
gato1 = Gato("Mimi")

print(cachorro1.som())
print(cachorro1.brincar())
print(gato1.som())
print(gato1.brincar())