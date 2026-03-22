from dataclasses import dataclass 
@dataclass
class Animal:
    nome:str
    def falar(self):
        print('Som genérico de animal!') 
    def apresentar(self):
        print(f'Eu sou um {self.nome} e digo: ',end='')
        self.falar()
class Cachorro(Animal):
    def falar(self):
        print('Au Au!')
class Gato(Animal):
    def falar(self):
        print('Miau!')
a=Animal('animal genérico') 
c = Cachorro('Rex')
g = Gato('Mimi')
a.apresentar()
c.apresentar()
g.apresentar()
