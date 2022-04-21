import abc
class Pessoa(abc.ABC):
    def __init__(self, nome, cpf, idade = int):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade

    def get_Nome(self):
        return self.__nome

    def set_Nome(self,nome):
        self.__nome = nome
    def get_Cpf(self):
        return self.__cpf

    def set_Cpf(self, cpf):
        self.__cpf = cpf

    def get_idade(self):
        return self.__idade

    def set_(self, idade):
        self.__idade = idade