import Leitor
class Colecao():
    def __init__(self,nome ,id_livros = [] , leitor = Leitor()):
        self.nome = nome
        self.id_livros = id_livros
        self.leitor = leitor