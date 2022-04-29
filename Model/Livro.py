import Leituras
class Livro():
    def __init__(self,titulo, autor, data_publicacao,paginas,sinopse,sbn, genero =[] ):
        self.__titulo = titulo
        self.__autor = autor
        self.__data_publicacao = data_publicacao
        self.__paginas = paginas
        self.__sinopse = sinopse
        self.__sbn = sbn
        self.__genero = genero
        self.leituras = Leituras(0, self)


    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_data_publicacao(self):
        return self.__data_publicacao

    def get_paginas(self):
        return self.__paginas

    def get_sinopse(self):
        return self.__sinopse

    def get_sbn(self):
        return self.__sbn

    def get_genero(self):
        return self.__genero

    def set_sinopse(self, nova_sinopse):
        self.__sinopse = nova_sinopse
