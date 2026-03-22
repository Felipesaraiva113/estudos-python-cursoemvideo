from dataclasses import dataclass 
@dataclass
class Pessoa:
    nome:str
    idade:int
    def apresentar(self):
        print(f'Olá, sou o {self.nome} e tenho {self.idade} anos.')
@dataclass
class Aluno(Pessoa):
    matricula: str
    curso: str
    def apresentar(self):
        print(f'Olá, sou o {self.nome}, tenho {self.idade} anos e estou matriculado no curso de {self.curso}. Matrícula: {self.matricula}')
pe = Pessoa('John',15)
a1 = Aluno('Felipe', 15, '2025001', 'Desenvolvimento de Sistemas')
@dataclass 
class Professor(Pessoa):
    salario:float 
    disciplina:str 
    def apresentar(self):
        print(f'Olá, sou o professor {self.nome}, tenho {self.idade} e leciono {self.disciplina}. Meu salário é {self.salario:.2f}.') 
p1 = Professor('Carlos',40,4500,'Matemática')
pe.apresentar()
a1.apresentar()
p1.apresentar()
