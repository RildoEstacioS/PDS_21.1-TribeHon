import Leitores
class Colecao():
    def __init__(self,nome ,id_livros = [] , leitor = Leitores()):
        self.nome = nome
        self.id_livros = id_livros
        self.leitor = leitor