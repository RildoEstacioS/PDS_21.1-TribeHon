import Livro
class Leituras():
    def __init__(self, ultima_pagina_lida, livro = Livro()):
        self.livro = livro
        self.ultima_pagina_lida = ultima_pagina_lida
