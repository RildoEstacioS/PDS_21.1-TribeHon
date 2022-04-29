import Autores
class Administrador(Autores):
    def __init__(self, nome_artitico,  login, senha, nome, cpf, nivel = int, idade = int):
        super(Administrador, self).__init__( nome_artitico,  login, senha, nome, cpf, nivel, idade )

    def bloqueiar_leitor(self):
        # Remove, treva ou bloqueia um leitor
        pass