from dataclasses import dataclass 
@dataclass
class Personagem:
    nome:str 
    vida: int        
@dataclass 
class Guerreiro(Personagem):
    forca:int 
    def atacar(self,a):
        a.vida-= self.forca
        print(f'{self.nome} atacou {a.nome} e causou {self.forca} de dano!')
    def status(self):
        print(f'Personagem: {self.nome} | Vida: {self.vida} | Força: {self.forca}')
@dataclass
class Mago(Personagem):
    mana:int 
    def atacar(self,a):
        if self.mana > 0:
            b = 30
        else:
            b = 0
        a.vida -= b
        print(f'{self.nome} atacou {a.nome} usando magia e causou {b} de dano!')
    def status(self):
        print(f'Personagem: {self.nome} | Vida: {self.vida} | Mana: {self.mana}')
g1 = Guerreiro(nome='Thor',vida=100,forca=20)
m1 = Mago(nome='Doutor Estranho',vida=80,mana=50)
g1.atacar(m1) 
m1.atacar(g1)
g1.status()
m1.status()
