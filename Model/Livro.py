from Model.Leitura import Leituras
class Livro():
    def __init__(self,titulo,sinopse, data_publicacao =int,paginas=int,sbn=int, genero = [] , autor = []):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao
        self.paginas = paginas
        self.sinopse = sinopse
        self.sbn = sbn
        self.genero = genero
        #self.leitura =Leituras(0, self, False)
