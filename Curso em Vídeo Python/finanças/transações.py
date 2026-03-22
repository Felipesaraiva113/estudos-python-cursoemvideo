from dataclasses import dataclass
from categoria import Categoria
@dataclass
class Transacao:
    descrição: str
    valor: float
    categoria: Categoria
    def exibir(self):
        print(f'descrição: {self.descrição} | valor: {self.valor} | categoria: {self.categoria.nome}')