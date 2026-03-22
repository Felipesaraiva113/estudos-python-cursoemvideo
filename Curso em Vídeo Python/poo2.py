from dataclasses import dataclass 
@dataclass
class Cliente:
    nome: str 
    email: str 
    idade: int
    def exibir(self):
        print(f'meu nome é {self.nome}, tenho {self.idade} anos e meu e-mail é: {self.email}')
fe = Cliente(nome='felipe',email='fe.emanuelsaraiva@gmail.com', idade=15)
fe.exibir()
