from model.Pessoa import Pessoa
from model.Colecao import Colecao

class Leitor(Pessoa):
    def __init__(self, login, senha, nome, cpf, nivel = int, idade = int ):
        super().__init__(nome, cpf, idade)
        self.login = login
        self.senha = senha
        self.nivel = nivel
        self.colecao = Colecao
        self.livros_lidos = int(0)
        self.paginas_lidas = 0
       # self.leitura = Leitura()



