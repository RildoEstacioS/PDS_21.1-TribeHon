#Classe Abstrata
import abc
class Pessoa(abc.ABC):
    def __init__(self, nome, cpf, idade = int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
