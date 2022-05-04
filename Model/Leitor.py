import Pessoa, Leitura, DAOColecoes, Colecao
class Leitor(Pessoa):
    def __init__(self, login, senha, nome, cpf, nivel = int, idade = int ):
        super().__init__(nome, cpf, idade)
        self.login = login
        self.senha = senha
        self.nivel = nivel
        self.colecao = Colecao()
        self.livros_lidos = int(0)
        self.paginas_lidas = 0
        self.leitura = Leitura()

    def ler_livro(self):
        # metodo responsavel pela busca na base e retorno de livor escolhido
        pass
    def criar_colecao(self, nome_da_colecao = str, lista_de_ids = []):
        DAOColecoes.criar_Colecao(nome_da_colecao,lista_de_ids, self)
        #Esse metodo gerara uma lista[] com os ids dos livros da basse e adicionara na colecao{}'''
        # metodo que possibilitara criar lista com varios livros
        #self.colecao(nome_da_colecao:lista_de_ids)


