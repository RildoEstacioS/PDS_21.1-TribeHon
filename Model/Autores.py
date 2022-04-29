import Leitores, Livro
class Autores (Leitores):
    def __init__(self, nome_artitico,  login, senha, nome, cpf, nivel = int, idade = int):
        super().__init__( login, senha, nome, cpf, nivel, idade )
        self.nome_artistico = nome_artitico

    def escrever_livro(self, livro = Livro()):
        #Falta codificar esse metodo que interage com a base
        pass