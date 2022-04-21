import Pessoa
class Leitor(Pessoa):
    def __init__(self, login, senha, nome, cpf, nivel = int, idade = int ):
        super().__init__(nome, cpf, idade)
        self.__login = login
        self.__senha = senha
        self.__nivel = nivel
        self.__colecao = {0:0}
        self.__livros_lidos = 0
        self.__paginas_lidas = 0

    def ler_livro(self):
        # metodo responsavel pela busca na base e retorno de livor escolhido
        pass
    def criar_colecao(self, nome_da_colecao = str, lista_de_ids = []):
        '''Esse metodo gerara uma lista[] com os ids dos livros da basse e adicionara na colecao{}'''
        # metodo que possibilitara criar lista com varios livros
        #self.colecao(nome_da_colecao:lista_de_ids)
        pass
    def get_login(self):
        return self.__login

    def get_senha(self):
        return self.__senha

    def get_nivel(self):
        return self.__nivel

    def get_livros_lidos(self):
        return self.__livros_lidos

    def get_lidas_lidas(self):
        return self.__paginas_lidas

    def get_colecao(self):
        return self.__colecao

    def set_colecao(self, colecao = {}):
        self.__colecao = colecao

    def adicionar_paginas(self, num_paginas = int):
        self.__paginas_lidas += num_paginas

    def adicionar_livros_lidos(self, num_livros):
        self.__livros_lidos += num_livros
    #criar gets e sets
